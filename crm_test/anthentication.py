from utils.request import Request
from exception_report import exception_agent
from utils.function_sort import FunctionSort
from utils.global_data import auto_wired,globaldata_productor
from logs.log_service import LogService
class Anthentication:
    def __init__(self) -> None:
        pass

    @exception_agent(module_name=__name__,path_name="/admin/login")
    @globaldata_productor(key="admin_request")
    def login_by_phone_password_0(self):
        params = {
            "phoneNumber":"+8613711111111",
            "password":"123456"
        }
        admin_request = Request()
        response = admin_request.get(params=params,url="/admin/login")
        Request.check_response(response=response)
        result = response.json()
        admin_request.set_authorization('{}{}'.format(result["data"]["tokenHead"],result["data"]["token"]))
        return admin_request
    
    @auto_wired
    def run__test(self,log_service:LogService=None):
        if log_service is not None:
            log_service.log('common','start testing the admin anthentication')
        function_orderer = FunctionSort([self])
        function_list = function_orderer.sort()
        for function in function_list:
            function()