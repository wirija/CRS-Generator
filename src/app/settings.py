# app/settings.py
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

try:
    import tomllib as tomli  # Python 3.11+
except ModuleNotFoundError:
    import tomli  # Python <= 3.10


CONFIG_PATH = Path(r"C:\Users\peter\Desktop\Internal Dev\CRS\CRS-Generator\src\config\CRS_validation.toml")
CRS_COUNTRYCODE_KEY = "CrsCountryCodeType"
CRS_CURRENCYCODE_KEY = "crsCurrCodeType"
CRS_ENTITYIDTYPE_KEY = 'CrsEntityIDTypeEnumType'
CRS_MSGTYPEINDIC_KEY = 'CrsMessageTypeIndicEnumType'
CRS_MSGTYPE_KEY = 'MessageTypeEnumType'

CRS_VALIDATION_KEY = 'validation'


@lru_cache(maxsize=1)
def get_validation_sets() -> dict[str, set[str]]:
    """
    Loads TOML once and returns normalized sets for membership checks.
    """
    with CONFIG_PATH.open("rb") as f:
        cfg = tomli.load(f)

    v = cfg[CRS_VALIDATION_KEY]

    return {
        CRS_ENTITYIDTYPE_KEY: {x.strip().upper() for x in v[CRS_ENTITYIDTYPE_KEY]},
        CRS_COUNTRYCODE_KEY: {x.strip().upper() for x in v[CRS_COUNTRYCODE_KEY]},
        CRS_COUNTRYCODE_KEY: {x.strip().upper() for x in v[CRS_COUNTRYCODE_KEY]},
    }