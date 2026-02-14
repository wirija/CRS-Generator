import openpyxl as xl
import pandas as pd
import os
from  config import (CRSSheets , MSGSPECS)
import reporting_schema.crs_xml_v2_0 as schema_crs

class CRS_Excel: 

    msg_spec = schema_crs.MessageSpecType()

    def __init__ (self, filepath:str):
        self.excel = None
        self.filepath = self.read_crs_xl(filepath)
        self.filepath_error = self.filepath.replace

        self.msg_spec  


    def read_crs_xl(self, filepath: str,) -> str:
        try:
            if os.path.isfile(filepath) and filepath.lower().endswith(("xls", "xlsx", "xlsm")):
                self.excel = xl.open(filepath)
                ## CHECK FOR ALL SHEET NAME 

                return filepath
            else:
                raise Exception("Error with file path")
        except Exception as e:
            return e
    
    def read_MessageSpec (self):
        try:
            df = pd.read_excel(self.filepath, sheet_name=CRSSheets.MSG_SPEC,)
            if len(msg_spec_dict) != 1:
                raise Exception("Number of entry should be 1")
            
            msg_spec_dict = df.iloc[0].to_dict()
            msg_spec_dict.update({key: '' for key in MSGSPECS.KEYS if key not in msg_spec_dict})

            # Validate the Message SpecType
            


            self.msg_spec = schema_crs.MessageSpecType(
                sending_company_in      = msg_spec_dict[MSGSPECS.SENDING_CO_IN], 
                transmitting_country    = msg_spec_dict[MSGSPECS.TRANS_COUNTRY],
                receiving_country       = msg_spec_dict[MSGSPECS.RECV_COUNTRY],
                message_type            = msg_spec_dict[MSGSPECS.MSG_TYPE],                     
                warning                 = msg_spec_dict[MSGSPECS.WARNING],             
                contact                 = msg_spec_dict[MSGSPECS.CONTACT],             
                message_ref_id          = msg_spec_dict[MSGSPECS.MSG_REF_ID],                     
                message_type_indic      = msg_spec_dict[MSGSPECS.MSG_TYPE_INDIC],                         
                corr_message_ref_id     = msg_spec_dict[MSGSPECS.CORR_TYPE_REF_ID],                         
                reporting_period        = msg_spec_dict[MSGSPECS.REPORTING_PERIOD],                         
                timestamp               = msg_spec_dict[MSGSPECS.TIMESTAMP],  
            )
        except Exception as e:
            return (e)

    def error 



