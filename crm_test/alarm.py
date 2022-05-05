from exception_report import exception_agent
from utils.request import Request
from logs.log_service import LogService
from utils.function_sort import FunctionSort
from utils.global_data import auto_wired
import time
class Alarm:
    
    def __init__(self) -> None:
        pass

    @exception_agent(module_name=__name__,path_name="/admin/alert/alarmList")
    @auto_wired
    def get_alarm_list_0(self,admin_request:Request=None):
        start_time = time.time()
        response = admin_request.get(url="/admin/alert/alarmList")
        end_time = time.time()
        seconds = end_time - start_time
        Request.check_response(response=response)
        if seconds > 120:
            raise Exception("alarmList loaded timeout: time costed -- {}s".format(seconds))

    @auto_wired
    def run__test(self,log_service:LogService=None):
        if log_service is not None:
            log_service.log('common','start testing the admin alarm')
        function_orderer = FunctionSort([self])
        function_list = function_orderer.sort()
        for function in function_list:
            function()