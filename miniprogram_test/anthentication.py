from utils.request import Request
from exception_report import exception_agent
from utils.function_sort import FunctionSort
from utils.global_data import auto_wired
from logs.log_service import LogService
from utils.global_data import globaldata_productor
class Anthentication:
    def __init__(self) -> None:
        pass

    @exception_agent(module_name=__name__,path_name="/user/loginByPhonePassword")
    @globaldata_productor(key="user_request")
    def login_by_phone_password_0(self):
        params = {
            "phoneNumber":"+8617626521182",
            "password":"123456"
        }
        user_request = Request()
        response = user_request.get(params=params,url="/user/loginByPhonePassword")
        Request.check_response(response=response)
        result = response.json()
        user_request.set_authorization(authorization='{}{}'.format(result["data"]["tokenHead"],result["data"]["token"]))
        return user_request
    
    @auto_wired
    def run__test(self,log_service:LogService=None):
        if log_service is not None:
            log_service.log('common','start testing the user anthentication')
        function_orderer = FunctionSort([self])
        function_list = function_orderer.sort()
        for function in function_list:
            function()