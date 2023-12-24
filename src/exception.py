import sys
import logging

from Tools.scripts.mailerdaemon import ErrorMessage # library will be available by default


def error_message_detail(error,error_detail:sys): ## creating customize error pop-up
    error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename  # please goo customer exception handling in python documantion 
    _,_,error_message = "Error Occured in python script name [{0}] line number [{1}] error message [{2}])".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomerException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

        def _str__(self):
            return self.error_message
        
    if __name__=='__main__':

        try:
            a=1/0
        except Exception as e:
            logging.info("Divide by Zero")
            raise CustomerException(e,sys)