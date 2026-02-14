# app/validation/validators.py
from __future__ import annotations

from typing import Callable, Optional, Any
from datetime import date, datetime
from pydantic_core.core_schema import ValidationInfo

ValidatorFn = Callable[[Any, ValidationInfo], str]
AllowedSupplier = Callable[[], set[str]]

 
# ----------------------------
# Small shared helpers
# ----------------------------
def _ensure_str(v: Any, label: str) -> str:
    if not isinstance(v, str):
        raise TypeError(f"{label} must be a string")
    return v


def _normalize(v: str, *, strip: bool = True, upper: bool = True) -> str:
    if strip:
        v = v.strip()
    if upper:
        v = v.upper()
    return v


# ----------------------------
# Generic validators
# ----------------------------
def make_in_set_validator(
    get_allowed: AllowedSupplier,
    *,
    label: str = "value",
    strip: bool = True,
    upper: bool = True,
) -> ValidatorFn:
    """
    Validates that the normalized string is in an allowed set.
    """

    def _validate(v: Any, _info: ValidationInfo) -> str:
        s = _normalize(_ensure_str(v, label), strip=strip, upper=upper)
        allowed = get_allowed()
        if s not in allowed:
            raise ValueError(f"Invalid {label}: '{s}'")
        return s

    return _validate


def make_fixed_length_validator(
    *,
    length: int,
    label: str = "value",
    strip: bool = True,
    upper: bool = True,
) -> ValidatorFn:
    """
    Validates that the normalized string has exactly `length` characters.
    """

    def _validate(v: Any, _info: ValidationInfo) -> str:
        s = _normalize(_ensure_str(v, label), strip=strip, upper=upper)
        if len(s) != length:
            raise ValueError(
                f"Invalid {label}: '{s}' length must be {length} characters"
            )
        return s

    return _validate


def make_iso_date_validator(
    *,
    label: str = "date",
    strip: bool = True,
) -> ValidatorFn:
    """
    Validates ISO date 'YYYY-MM-DD'. Returns canonical 'YYYY-MM-DD'.
    """

    def _validate(v: Any, _info: ValidationInfo) -> str:
        s = _normalize(_ensure_str(v, label), strip=strip, upper=False)
        try:
            d = date.fromisoformat(s)  # expects YYYY-MM-DD
        except ValueError:
            raise ValueError(f"Invalid {label}: '{s}' must be in format YYYY-MM-DD")
        return d.isoformat()

    return _validate


def make_iso_datetime_validator(
    *,
    label: str = "datetime",
    strip: bool = True,
    require_seconds: bool = True,
) -> ValidatorFn:
    """
    Validates ISO datetime. Your CRS format appears to be 'YYYY-MM-DDThh:mm:ss'.
    - Uses datetime.fromisoformat (fast + correct)
    - Optionally requires seconds component
    Returns canonical 'YYYY-MM-DDTHH:MM:SS' (seconds included).
    """

    def _validate(v: Any, _info: ValidationInfo) -> str:
        s = _normalize(_ensure_str(v, label), strip=strip, upper=False)

        # enforce 'T' separator if required spec
        if "T" not in s:
            raise ValueError(
                f"Invalid {label}: '{s}' must be in format YYYY-MM-DDThh:mm:ss"
            )

        try:
            dt = datetime.fromisoformat(
                s
            )  # accepts 'YYYY-MM-DDTHH:MM[:SS[.ffffff]][+HH:MM]'
        except ValueError:
            raise ValueError(
                f"Invalid {label}: '{s}' must be in format YYYY-MM-DDThh:mm:ss"
            )

        # If you strictly require seconds, enforce it:
        # fromisoformat allows 'HH:MM' — your CRS wants 'HH:MM:SS'
        if require_seconds:
            time_part = s.split("T", 1)[1]
            # remove timezone for counting, if you ever allow it
            time_core = time_part.split("+", 1)[0].split("-", 1)[0].split("Z", 1)[0]
            if time_core.count(":") != 2:
                raise ValueError(
                    f"Invalid {label}: '{s}' must include seconds (HH:MM:SS)"
                )

        # Canonicalize: keep seconds, drop microseconds
        dt = dt.replace(microsecond=0)
        return dt.isoformat()

    return _validate


# ----------------------------
# CRS-specific validators
# ----------------------------
def make_sending_company_in_validator(
    get_allowed_entity_types: AllowedSupplier,
    *,
    label: str = "SendingCompanyIN",
) -> ValidatorFn:
    """
    Validates and canonicalizes:
      '<EntityIDType> <EntityID>'
    - EntityIDType must be in allowed set
    - EntityID must be non-empty
    Returns canonical: 'ENTITYIDTYPE EntityID'
    """

    def _validate(v: Any, _info: ValidationInfo) -> str:
        raw = _ensure_str(v, label).strip()
        parts = raw.split()  # collapses multiple spaces
        if len(parts) != 2:
            raise ValueError(f"{label} must be in format '<EntityIDType> <EntityID>'")

        entity_id_type = parts[0].strip().upper()
        entity_id = parts[1].strip()

        allowed = {x.upper() for x in get_allowed_entity_types()}
        if entity_id_type not in allowed:
            raise ValueError(f"Invalid Entity ID Type: '{entity_id_type}'")

        if not entity_id:
            raise ValueError("EntityID must not be blank")

        return f"{entity_id_type} {entity_id}"

    return _validate
