from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from src.reporting_schema.common_types_fatca_crs_v2_0 import MonAmntType
from src.reporting_schema.oecdcrstypes_v5_0 import DocSpecType

__NAMESPACE__ = "urn:oecd:ties:fatca:v1"


class FatcaAcctPoolReportTypeEnumType(Enum):
    """
    Account Pool Reporting Type.

    :cvar FATCA201: Recalcitrant account holders with US Indicia
    :cvar FATCA202: Recalcitrant account holders without US Indicia
    :cvar FATCA203: Dormant accounts
    :cvar FATCA204: Non-participating foreign financial institutions
    :cvar FATCA205: Recalcitrant account holders that are US persons
    :cvar FATCA206: Recalcitrant account holders that are passive NFFEs
    """
 
    FATCA201 = "FATCA201"
    FATCA202 = "FATCA202"
    FATCA203 = "FATCA203"
    FATCA204 = "FATCA204"
    FATCA205 = "FATCA205"
    FATCA206 = "FATCA206"


@dataclass(kw_only=True)
class CorrectablePoolReportType:
    class Meta:
        name = "CorrectablePoolReport_Type"

    doc_spec: DocSpecType = field(
        metadata={
            "name": "DocSpec",
            "type": "Element",
            "namespace": "urn:oecd:ties:fatca:v1",
            "required": True,
        }
    )
    account_count: int = field(
        metadata={
            "name": "AccountCount",
            "type": "Element",
            "namespace": "urn:oecd:ties:fatca:v1",
            "required": True,
        }
    )
    account_pool_report_type: FatcaAcctPoolReportTypeEnumType = field(
        metadata={
            "name": "AccountPoolReportType",
            "type": "Element",
            "namespace": "urn:oecd:ties:fatca:v1",
            "required": True,
        }
    )
    pool_balance: MonAmntType = field(
        metadata={
            "name": "PoolBalance",
            "type": "Element",
            "namespace": "urn:oecd:ties:fatca:v1",
            "required": True,
        }
    )
