from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate, XmlDateTime

from src.reporting_schema.common_types_fatca_crs_v2_0 import (
    AcctNumberTypeEnumType,
    AddressType,
    MonAmntType,
    NameOrganisationType,
    TinType,
)
from src.reporting_schema.fatca_types_v1_2 import CorrectablePoolReportType
from src.reporting_schema.isocrstypes_v1_1 import CountryCodeType
from src.reporting_schema.oecdcrstypes_v5_0 import (
    DocSpecType,
    OecdnameTypeEnumType,
) 

__NAMESPACE__ = "urn:oecd:ties:crs:v2"


class CrsAcctHolderTypeEnumType(Enum):
    """
    Account Holder Type.

    :cvar CRS101: Passive Non-Financial Entity with one or more
        controlling person that is a Reportable Person
    :cvar CRS102: CRS Reportable Person
    :cvar CRS103: Passive NFE that is a CRS Reportable Person
    """

    CRS101 = "CRS101"
    CRS102 = "CRS102"
    CRS103 = "CRS103"


class CrsCtrlgPersonTypeEnumType(Enum):
    """
    Controlling Person Type.

    :cvar CRS801: CP of legal person - ownership
    :cvar CRS802: CP of legal person - other means
    :cvar CRS803: CP of legal person - senior managing official
    :cvar CRS804: CP of legal arrangement - trust - settlor
    :cvar CRS805: CP of legal arrangement - trust - trustee
    :cvar CRS806: CP of legal arrangement - trust - protector
    :cvar CRS807: CP of legal arrangement - trust - beneficiary
    :cvar CRS808: CP of legal arrangement - trust - other
    :cvar CRS809: CP of legal arrangement - other - settlor-equivalent
    :cvar CRS810: CP of legal arrangement - other - trustee-equivalent
    :cvar CRS811: CP of legal arrangement - other - protector-equivalent
    :cvar CRS812: CP of legal arrangement - other - beneficiary-
        equivalent
    :cvar CRS813: CP of legal arrangement - other - other-equivalent
    """

    CRS801 = "CRS801"
    CRS802 = "CRS802"
    CRS803 = "CRS803"
    CRS804 = "CRS804"
    CRS805 = "CRS805"
    CRS806 = "CRS806"
    CRS807 = "CRS807"
    CRS808 = "CRS808"
    CRS809 = "CRS809"
    CRS810 = "CRS810"
    CRS811 = "CRS811"
    CRS812 = "CRS812"
    CRS813 = "CRS813"


class CrsMessageTypeIndicEnumType(Enum):
    """
    The MessageTypeIndic defines the type of message sent.

    :cvar CRS701: The message contains new information
    :cvar CRS702: The message contains corrections for previously sent
        information
    :cvar CRS703: The message advises there is no data to report
    """

    CRS701 = "CRS701"
    CRS702 = "CRS702"
    CRS703 = "CRS703"


class CrsPaymentTypeEnumType(Enum):
    """
    The code describing the nature of the payments used in CRS.

    :cvar CRS501: Dividends
    :cvar CRS502: Interest
    :cvar CRS503: Gross Proceeds/Redemptions
    :cvar CRS504: Other - CRS
    """

    CRS501 = "CRS501"
    CRS502 = "CRS502"
    CRS503 = "CRS503"
    CRS504 = "CRS504"


class MessageTypeEnumType(Enum):
    """
    Message type defines the type of reporting.
    """

    CRS = "CRS"


@dataclass(kw_only=True)
class FiaccountNumberType:
    """
    Account number definition.

    :ivar value:
    :ivar acct_number_type: Account Number Type
    :ivar undocumented_account: Undocumented Account
    :ivar closed_account: Closed Account
    :ivar dormant_account: Dormant Account
    """

    class Meta:
        name = "FIAccountNumber_Type"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 200,
        },
    )
    acct_number_type: None | AcctNumberTypeEnumType = field(
        default=None,
        metadata={
            "name": "AcctNumberType",
            "type": "Attribute",
        },
    )
    undocumented_account: None | bool = field(
        default=None,
        metadata={
            "name": "UndocumentedAccount",
            "type": "Attribute",
        },
    )
    closed_account: None | bool = field(
        default=None,
        metadata={
            "name": "ClosedAccount",
            "type": "Attribute",
        },
    )
    dormant_account: None | bool = field(
        default=None,
        metadata={
            "name": "DormantAccount",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class MessageSpecType:
    """
    Information in the message header identifies the Tax Administration
    that is sending the message.

    It specifies when the message was created, what period (normally a
    year) the report is for, and the nature of the report (original,
    corrected, supplemental, etc).

    :ivar sending_company_in:
    :ivar transmitting_country:
    :ivar receiving_country:
    :ivar message_type:
    :ivar warning: Free text expressing the restrictions for use of the
        information this message contains and the legal framework under
        which it is given
    :ivar contact: All necessary contact information about persons
        responsible for and involved in the processing of the data
        transmitted in this message, both legally and technically. Free
        text as this is not intended for automatic processing.
    :ivar message_ref_id: Sender's unique identifier for this message
    :ivar message_type_indic:
    :ivar corr_message_ref_id: Sender's unique identifier that has to be
        corrected.  Must point to 1 or more previous message
    :ivar reporting_period: The reporting year for which information is
        transmitted in documents of the current message.
    :ivar timestamp:
    """

    class Meta:
        name = "MessageSpec_Type"

    sending_company_in: None | str = field(
        default=None,
        metadata={
            "name": "SendingCompanyIN",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_length": 1,
            "max_length": 200,
        },
    )
    transmitting_country: CountryCodeType = field(
        metadata={
            "name": "TransmittingCountry",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    receiving_country: CountryCodeType = field(
        metadata={
            "name": "ReceivingCountry",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    message_type: MessageTypeEnumType = field(
        metadata={
            "name": "MessageType",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    warning: None | str = field(
        default=None,
        metadata={
            "name": "Warning",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_length": 1,
            "max_length": 4000,
        },
    )
    contact: None | str = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_length": 1,
            "max_length": 4000,
        },
    )
    message_ref_id: str = field(
        metadata={
            "name": "MessageRefId",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
            "min_length": 1,
            "max_length": 170,
        }
    )
    message_type_indic: CrsMessageTypeIndicEnumType = field(
        metadata={
            "name": "MessageTypeIndic",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    corr_message_ref_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CorrMessageRefId",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_length": 1,
            "max_length": 170,
        },
    )
    reporting_period: XmlDate = field(
        metadata={
            "name": "ReportingPeriod",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    timestamp: XmlDateTime = field(
        metadata={
            "name": "Timestamp",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class NamePersonType:
    """
    The user must spread the data about the name of a party over up to six
    elements.

    The container element for this will be 'NameFix'.

    :ivar preceding_title: His Excellency,Estate of the Late ...
    :ivar title: Greeting title. Example: Mr, Dr, Ms, Herr, etc. Can
        have multiple titles.
    :ivar first_name: FirstName of the person
    :ivar middle_name: Middle name (essential part of the name for many
        nationalities). Example: Sakthi in "Nivetha Sakthi Shantha". Can
        have multiple middle names.
    :ivar name_prefix: de, van, van de, von, etc. Example: Derick de
        Clarke
    :ivar last_name: Represents the position of the name in a name
        string. Can be Given Name, Forename, Christian Name, Surname,
        Family Name, etc. Use the attribute "NameType" to define what
        type this name is. In case of a company, this field can be used
        for the company name.
    :ivar generation_identifier: Jnr, Thr Third, III
    :ivar suffix: Could be compressed initials - PhD, VC, QC
    :ivar general_suffix: Deceased, Retired ...
    :ivar name_type:
    """

    class Meta:
        name = "NamePerson_Type"

    preceding_title: None | str = field(
        default=None,
        metadata={
            "name": "PrecedingTitle",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_length": 1,
            "max_length": 200,
        },
    )
    title: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_length": 1,
            "max_length": 200,
        },
    )
    first_name: NamePersonType.FirstName = field(
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    middle_name: list[NamePersonType.MiddleName] = field(
        default_factory=list,
        metadata={
            "name": "MiddleName",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
        },
    )
    name_prefix: None | NamePersonType.NamePrefix = field(
        default=None,
        metadata={
            "name": "NamePrefix",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
        },
    )
    last_name: NamePersonType.LastName = field(
        metadata={
            "name": "LastName",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    generation_identifier: list[str] = field(
        default_factory=list,
        metadata={
            "name": "GenerationIdentifier",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_length": 1,
            "max_length": 200,
        },
    )
    suffix: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Suffix",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_length": 1,
            "max_length": 200,
        },
    )
    general_suffix: None | str = field(
        default=None,
        metadata={
            "name": "GeneralSuffix",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_length": 1,
            "max_length": 200,
        },
    )
    name_type: None | OecdnameTypeEnumType = field(
        default=None,
        metadata={
            "name": "nameType",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class FirstName:
        """
        :ivar value:
        :ivar xnl_name_type: Defines the name type of FirstName.
            Example: Given Name, Forename, Christian Name, Father's
            Name, etc. In some countries, FirstName could be a Family
            Name or a SurName. Use this attribute to define the type for
            this name.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 1,
                "max_length": 200,
            },
        )
        xnl_name_type: None | str = field(
            default=None,
            metadata={
                "name": "xnlNameType",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 200,
            },
        )

    @dataclass(kw_only=True)
    class MiddleName:
        """
        :ivar value:
        :ivar xnl_name_type: Defines the name type of Middle Name.
            Example: First name, middle name, maiden name, father's
            name, given name, etc.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 1,
                "max_length": 200,
            },
        )
        xnl_name_type: None | str = field(
            default=None,
            metadata={
                "name": "xnlNameType",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 200,
            },
        )

    @dataclass(kw_only=True)
    class NamePrefix:
        """
        :ivar value:
        :ivar xnl_name_type: Defines the type of name associated with
            the NamePrefix. For example the type of name is LastName and
            this prefix is the prefix for this last name.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 1,
                "max_length": 200,
            },
        )
        xnl_name_type: None | str = field(
            default=None,
            metadata={
                "name": "xnlNameType",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 200,
            },
        )

    @dataclass(kw_only=True)
    class LastName:
        """
        :ivar value:
        :ivar xnl_name_type: Defines the name type of LastName. Example:
            Father's name, Family name, Sur Name, Mother's Name, etc. In
            some countries, LastName could be the given name or first
            name.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 1,
                "max_length": 200,
            },
        )
        xnl_name_type: None | str = field(
            default=None,
            metadata={
                "name": "xnlNameType",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 200,
            },
        )


@dataclass(kw_only=True)
class OrganisationInType:
    """
    This is the identification number/identification code for the Entity in
    question.

    As the identifier may be not strictly numeric, it is just defined as a
    string of characters. Attribute 'issuedBy' is required to designate the
    issuer of the identifier. Attribute 'INType' defines the type of
    identification number.

    :ivar value:
    :ivar issued_by: Country code of issuing country, indicating country
        of Residence (to taxes and other)
    :ivar intype: Identification Number Type
    """

    class Meta:
        name = "OrganisationIN_Type"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 200,
        },
    )
    issued_by: None | CountryCodeType = field(
        default=None,
        metadata={
            "name": "issuedBy",
            "type": "Attribute",
        },
    )
    intype: None | str = field(
        default=None,
        metadata={
            "name": "INType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 200,
        },
    )


@dataclass(kw_only=True)
class PaymentType:
    """
    :ivar type_value: Type of payment (interest, dividend,...)
    :ivar payment_amnt: The amount of payment
    """

    class Meta:
        name = "Payment_Type"

    type_value: CrsPaymentTypeEnumType = field(
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    payment_amnt: MonAmntType = field(
        metadata={
            "name": "PaymentAmnt",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrganisationPartyType:
    """
    This container brings together all data about an organisation as a
    party.

    Name and address are required components and each can be present more
    than once to enable as complete a description as possible. Whenever
    possible one or more identifiers (TIN etc) should be added as well as a
    residence country code. Additional data that describes and identifies
    the party can be given . The code for the legal type according to the
    OECD codelist must be added. The structures of all of the subelements
    are defined elsewhere in this schema.

    :ivar res_country_code:
    :ivar in_value: Entity Identification Number
    :ivar name:
    :ivar address:
    """

    class Meta:
        name = "OrganisationParty_Type"

    res_country_code: list[CountryCodeType] = field(
        default_factory=list,
        metadata={
            "name": "ResCountryCode",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
        },
    )
    in_value: list[OrganisationInType] = field(
        default_factory=list,
        metadata={
            "name": "IN",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
        },
    )
    name: list[NameOrganisationType] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_occurs": 1,
        },
    )
    address: list[AddressType] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PersonPartyType:
    """
    This container brings together all data about a person as a party.

    Name and address are required components and each can be present more
    than once to enable as complete a description as possible. Whenever
    possible one or more identifiers (TIN etc) should be added as well as a
    residence country code. Additional data that describes and identifies
    the party can be given. The code for the legal type according to the
    OECD codelist must be added. The structures of all of the subelements
    are defined elsewhere in this schema.
    """

    class Meta:
        name = "PersonParty_Type"

    res_country_code: list[CountryCodeType] = field(
        default_factory=list,
        metadata={
            "name": "ResCountryCode",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_occurs": 1,
        },
    )
    tin: list[TinType] = field(
        default_factory=list,
        metadata={
            "name": "TIN",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
        },
    )
    name: list[NamePersonType] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_occurs": 1,
        },
    )
    address: list[AddressType] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_occurs": 1,
        },
    )
    nationality: list[CountryCodeType] = field(
        default_factory=list,
        metadata={
            "name": "Nationality",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
        },
    )
    birth_info: None | PersonPartyType.BirthInfo = field(
        default=None,
        metadata={
            "name": "BirthInfo",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
        },
    )

    @dataclass(kw_only=True)
    class BirthInfo:
        birth_date: None | XmlDate = field(
            default=None,
            metadata={
                "name": "BirthDate",
                "type": "Element",
                "namespace": "urn:oecd:ties:crs:v2",
            },
        )
        city: None | str = field(
            default=None,
            metadata={
                "name": "City",
                "type": "Element",
                "namespace": "urn:oecd:ties:crs:v2",
                "min_length": 1,
                "max_length": 200,
            },
        )
        city_subentity: None | str = field(
            default=None,
            metadata={
                "name": "CitySubentity",
                "type": "Element",
                "namespace": "urn:oecd:ties:crs:v2",
                "min_length": 1,
                "max_length": 200,
            },
        )
        country_info: None | PersonPartyType.BirthInfo.CountryInfo = field(
            default=None,
            metadata={
                "name": "CountryInfo",
                "type": "Element",
                "namespace": "urn:oecd:ties:crs:v2",
            },
        )

        @dataclass(kw_only=True)
        class CountryInfo:
            country_code: None | CountryCodeType = field(
                default=None,
                metadata={
                    "name": "CountryCode",
                    "type": "Element",
                    "namespace": "urn:oecd:ties:crs:v2",
                },
            )
            former_country_name: None | str = field(
                default=None,
                metadata={
                    "name": "FormerCountryName",
                    "type": "Element",
                    "namespace": "urn:oecd:ties:crs:v2",
                    "min_length": 1,
                    "max_length": 200,
                },
            )


@dataclass(kw_only=True)
class AccountHolderType:
    class Meta:
        name = "AccountHolder_Type"

    individual: None | PersonPartyType = field(
        default=None,
        metadata={
            "name": "Individual",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
        },
    )
    organisation: None | OrganisationPartyType = field(
        default=None,
        metadata={
            "name": "Organisation",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
        },
    )
    acct_holder_type: None | CrsAcctHolderTypeEnumType = field(
        default=None,
        metadata={
            "name": "AcctHolderType",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
        },
    )


@dataclass(kw_only=True)
class ControllingPersonType:
    class Meta:
        name = "ControllingPerson_Type"

    individual: PersonPartyType = field(
        metadata={
            "name": "Individual",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    ctrlg_person_type: None | CrsCtrlgPersonTypeEnumType = field(
        default=None,
        metadata={
            "name": "CtrlgPersonType",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
        },
    )


@dataclass(kw_only=True)
class CorrectableOrganisationPartyType(OrganisationPartyType):
    class Meta:
        name = "CorrectableOrganisationParty_Type"

    doc_spec: DocSpecType = field(
        metadata={
            "name": "DocSpec",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CorrectableAccountReportType:
    class Meta:
        name = "CorrectableAccountReport_Type"

    doc_spec: DocSpecType = field(
        metadata={
            "name": "DocSpec",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    account_number: FiaccountNumberType = field(
        metadata={
            "name": "AccountNumber",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    account_holder: AccountHolderType = field(
        metadata={
            "name": "AccountHolder",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    controlling_person: list[ControllingPersonType] = field(
        default_factory=list,
        metadata={
            "name": "ControllingPerson",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
        },
    )
    account_balance: MonAmntType = field(
        metadata={
            "name": "AccountBalance",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    payment: list[PaymentType] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
        },
    )


@dataclass(kw_only=True)
class CrsBodyType:
    """
    :ivar reporting_fi: Reporting financial institution
    :ivar reporting_group: For CRS, only one ReportingGroup for each
        CrsBody is to be provided
    """

    class Meta:
        name = "CrsBody_Type"

    reporting_fi: CorrectableOrganisationPartyType = field(
        metadata={
            "name": "ReportingFI",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "required": True,
        }
    )
    reporting_group: list[CrsBodyType.ReportingGroup] = field(
        default_factory=list,
        metadata={
            "name": "ReportingGroup",
            "type": "Element",
            "namespace": "urn:oecd:ties:crs:v2",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class ReportingGroup:
        sponsor: None | CorrectableOrganisationPartyType = field(
            default=None,
            metadata={
                "name": "Sponsor",
                "type": "Element",
                "namespace": "urn:oecd:ties:crs:v2",
            },
        )
        intermediary: None | CorrectableOrganisationPartyType = field(
            default=None,
            metadata={
                "name": "Intermediary",
                "type": "Element",
                "namespace": "urn:oecd:ties:crs:v2",
            },
        )
        account_report: list[CorrectableAccountReportType] = field(
            default_factory=list,
            metadata={
                "name": "AccountReport",
                "type": "Element",
                "namespace": "urn:oecd:ties:crs:v2",
            },
        )
        pool_report: list[CorrectablePoolReportType] = field(
            default_factory=list,
            metadata={
                "name": "PoolReport",
                "type": "Element",
                "namespace": "urn:oecd:ties:crs:v2",
            },
        )


@dataclass(kw_only=True)
class CrsOecd:
    """
    :ivar message_spec:
    :ivar crs_body:
    :ivar version: CRS Version
    """

    class Meta:
        name = "CRS_OECD"
        namespace = "urn:oecd:ties:crs:v2"

    message_spec: MessageSpecType = field(
        metadata={
            "name": "MessageSpec",
            "type": "Element",
            "required": True,
        }
    )
    crs_body: list[CrsBodyType] = field(
        default_factory=list,
        metadata={
            "name": "CrsBody",
            "type": "Element",
        },
    )
    version: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        },
    )
