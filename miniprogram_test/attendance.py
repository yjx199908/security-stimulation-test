from datetime import datetime
from utils.request import Request
from utils.global_data import auto_wired,globaldata_productor,GlobalData
from exception_report import exception_agent
from utils.function_sort import FunctionSort
from utils.compute_utils import compute_fence_center
from utils.global_constant import GlobalConstant
from logs.log_service import LogService
from utils.img_provide import ImgProvider
class Attendance:
    def __init__(self) -> None:
        pass

    @exception_agent(module_name=__name__,path_name="/user/attendance/fence")
    @globaldata_productor(key="user_fence")
    @auto_wired
    def get_fence_0(self,user_request:Request=None):
        response = user_request.get(url="/user/attendance/fence")
        Request.check_response(response=response)
        result = response.json()
        return result["data"]

    @globaldata_productor(key="attendance_point")
    @exception_agent(module_name=__name__,path_name="/user/attendance/location/monitor")
    @auto_wired
    def location_report_1(self,user_fence=[],attendance_point=None,user_request:Request=None):
        [duty_fence,task_fence] = user_fence
        fence = duty_fence or task_fence
         # use duty fence now
        latitude,longitude = attendance_point or compute_fence_center(fence)
        data = {
            "longitude":longitude,
            "latitude":latitude,
            "isOverstep":GlobalConstant.IN_BOUND
        }
        user_request.post_with_json(url="/user/attendance/location/monitor",json=data)
        return (latitude,longitude)
        
    @globaldata_productor(key="attendance_id")
    @exception_agent(module_name=__name__,path_name="/user/attendance/attend")
    @auto_wired
    def attendance_2(self,user_fence=[],attendance_point=None,user_request:Request=None):
        is_on_work = False
        if GlobalData.contains("on_off_work"):
            is_on_work = GlobalData.get_status("is_on_work")
        on_off_work = 1
        if is_on_work:
            on_off_work = 0
        [duty_fence,task_fence] = user_fence
        fence = duty_fence or task_fence
        # use duty fence now
        latitude,longitude = attendance_point or compute_fence_center(fence)
        data = {
            "longitude":longitude,
            "latitude":latitude,
            "locationName":GlobalConstant.LOCATION_NAME,
            "type":GlobalConstant.DUTY_ATTENDANCE,
            "onOffWork":on_off_work
        }
        response = user_request.post_with_json(url="/user/attendance/attend",json=data)
        Request.check_response(response=response)
        attendance_id = response.json()["data"]["id"]
        GlobalData.set_status("is_on_work",not is_on_work)
        return attendance_id
    
    @exception_agent(module_name=__name__,path_name="/user/attendance/uploadAttendancePhoto")
    @auto_wired
    def upload_attendance_photo_3(self,attendance_id=None,log_service:LogService=None,user_request:Request=None):
        if attendance_id is None and log_service is not None:
            log_service.log(kind='error',content="there isn't the variable named attendance_id in container, skip this step")
            return
        ImgProvider.draw(content=GlobalConstant.ATTENDANCE_PHOTO_CONTENT_TEMPLATE.format(datetime.now().strftime('%x %X')),img_name='attendance_photo.jpg')
        files = {
            'file': open('./attendance_photo.jpg', 'rb')
        }
        data = {
            'attendanceId':attendance_id
        }
        response = user_request.post_with_formdata(url="/user/attendance/uploadAttendancePhoto",files=files,data=data)
        Request.check_response(response=response)
        a = 1/0

    @auto_wired
    def run__test(self,log_service:LogService=None):
        if log_service is not None:
            log_service.log('common','start testing the attendance module')
        function_orderer = FunctionSort([self])
        function_list = function_orderer.sort()
        for function in function_list:
            function()
        