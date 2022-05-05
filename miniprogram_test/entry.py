from .anthentication import Anthentication
from .attendance import Attendance
from logs.log_service import LogService
from utils.global_data import auto_wired
from exception_report import exception_agent

class MiniProgramTestEntry:
    def __init__(self) -> None:
        pass
    
    @exception_agent(module_name=__name__,path_name='WXminiprogram test system')
    @auto_wired
    def start(self,log_service:LogService=None):
        log_service.log(kind='common',content='WXminiprogram test system launched!')
        anthentication = Anthentication()
        anthentication.run__test()
        attendance = Attendance()
        attendance.run__test()
        log_service.log(kind='common',content='Wxminiprogram test system ended!')