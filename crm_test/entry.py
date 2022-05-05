from logs.log_service import LogService
from utils.global_data import auto_wired
from exception_report import exception_agent
from crm_test.anthentication import Anthentication
from crm_test.alarm import Alarm
class CrmTestEntry:
    def __init__(self) -> None:
        pass

    @exception_agent(module_name=__name__,path_name='crm test system')
    @auto_wired
    def start(self,log_service:LogService=None):
        log_service.log(kind='common',content='crm test system started!')
        anthentication = Anthentication()
        anthentication.run__test()
        alarm = Alarm()
        alarm.run__test()
        log_service.log(kind='common',content='crm test system ended!')
