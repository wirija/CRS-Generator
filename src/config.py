

class CRSSheets:
    MSG_SPEC  = 'Message Header'
    REPORTING_FI = 'Reporting FI'

class VALIDATION_RULES:
    LENGTH_1_200 =  'length1_200' #Length should only be from 1 to 200
    LENGTH_1_4000 =  'length1_4000' #Length should only be from 1 to 200
    ISO_COUNTRY_TYPE =  'ISO country' # can only use countries from ISO Country
    ENUM_CRS = 'CRS'
    BLANK = 'Blank' # should be left blank for IRAS Reporting

 
class MSGSPECS:
    SENDING_CO_IN = 'SendingCompanyIN'
    TRANS_COUNTRY = 'TransmittingCountry'
    RECV_COUNTRY = 'ReceivingCountry'
    MSG_TYPE  = 'MessageType'
    WARNING  = 'Warning'
    CONTACT  = 'Contact'
    MSG_REF_ID  = 'MessageRefID'
    MSG_TYPE_INDIC = "MessageTypeIndic"
    CORR_TYPE_REF_ID = "corr_message_ref_id" #Not used for CRS
    REPORTING_PERIOD = "ReportingPeriod"
    TIMESTAMP = "Timestamp"
    KEYS = [
          SENDING_CO_IN
        , TRANS_COUNTRY
        , RECV_COUNTRY
        , MSG_TYPE
        , WARNING
        , CONTACT
        , MSG_REF_ID
        , MSG_TYPE_INDIC
        , CORR_TYPE_REF_ID
        , REPORTING_PERIOD
        , TIMESTAMP
    ]
