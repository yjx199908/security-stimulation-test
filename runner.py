from crm_test.entry import CrmTestEntry
from miniprogram_test.entry import MiniProgramTestEntry
from utils.global_data import auto_wired
from utils.argument_analysis import ArgumentAnalysiser

@auto_wired
def run(rt_arg_getter:ArgumentAnalysiser=None):
    crm_test_entry = CrmTestEntry()
    mini_program_test_entry = MiniProgramTestEntry()
    mini_program_test_entry.start()
    crm_test_entry.start()
    