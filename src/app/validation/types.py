# app/validation/types.py
from __future__ import annotations

from typing import Annotated, Callable
from pydantic import BeforeValidator

from src.app.settings import get_validation_sets
from src.app.validation.validators import (
    make_in_set_validator,
    make_sending_company_in_validator,
    make_fixed_length_validator,
    make_iso_date_validator,
    make_iso_datetime_validator,
) 

AllowedSupplier = Callable[[], set[str]]

def allowed(key: str) -> AllowedSupplier:
    """Return a callable that supplies an allowed set from cached validation config."""
    return lambda: get_validation_sets()[key]


CountryCode = Annotated[
    str,
    BeforeValidator(
        make_in_set_validator(
            allowed("country_codes"),
            label="Country Code",
        )
    ),
]

CurrencyCode = Annotated[
    str,
    BeforeValidator(
        make_in_set_validator(
            allowed("currency_codes"),
            label="Currency Code",
        )
    ),
]

SendingCompanyIN = Annotated[
    str,
    BeforeValidator(
        make_sending_company_in_validator(
            allowed("entity_id_types"),
            label="SendingCompanyIN",
        )
    ),
]

MessageRefID = Annotated[
    str,
    BeforeValidator(
        make_fixed_length_validator(
            length=25,
            label="MessageRefID",
        )
    ),
]

MessageTypeIndic = Annotated[
    str,
    BeforeValidator(
        make_in_set_validator(
            allowed("message_type_indic"),
            label="MessageTypeIndic",
        )
    ),
]

MessageType = Annotated[
    str,
    BeforeValidator(
        make_in_set_validator(
            allowed("message_types"),
            label="MessageType",
        )
    ),
]

ReportingPeriod = Annotated[
    str,
    BeforeValidator(
        make_iso_date_validator(
            label="ReportingPeriod",
        )
    ),
]

Timestamp = Annotated[
    str,
    BeforeValidator(
        make_iso_datetime_validator(
            label="Timestamp",
            require_seconds=True,  # CRS usually wants HH:MM:SS
        )
    ),
]