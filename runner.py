from crm_test.entry import CrmTestEntry
from miniprogram_test.entry import MiniProgramTestEntry
from utils.global_data import auto_wired,GlobalData
from utils.argument_analysis import ArgumentAnalysiser
from exception_report import exception_agent
import time

@exception_agent(module_name="runner",path_name="None")
@auto_wired
def run(rt_arg_getter:ArgumentAnalysiser=None):
    interval = int(rt_arg_getter.get("--interval"))
    while True:
        crm_test_entry = CrmTestEntry()
        mini_program_test_entry = MiniProgramTestEntry()
        mini_program_test_entry.start()
        crm_test_entry.start()
        time.sleep(interval)