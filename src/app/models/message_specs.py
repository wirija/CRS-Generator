# src/app/model/message_specs.py

from pydantic import BaseModel,  ConfigDict
from pydantic import BaseModel
from src.app.validation.types import (
    CountryCode,
    SendingCompanyIN,
    MessageType,
    MessageRefID,
    MessageTypeIndic,
    ReportingPeriod,
    Timestamp,
)


class MessageSpecs(BaseModel):
    model_config = ConfigDict(extra="forbid")  # optional: reject unknown fields

    SendingCompanyIN: SendingCompanyIN
    TransmittingCountry: CountryCode
    ReceivingCountry: CountryCode
    MessageType: MessageType
    Warning: str = ''
    Contact: str = ''
    MessageRefID: MessageRefID
    MessageTypeIndic: MessageTypeIndic
    corr_message_ref_id: str = '' 
    ReportingPeriod: ReportingPeriod
    Timestamp: Timestamp