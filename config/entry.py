import sys
from logs.log_service import LogService
from utils.function_sort import FunctionSort
from utils.global_data import globaldata_productor
from utils.argument_analysis import ArgumentAnalysiser

class Configuration:
    def __init__(self) -> None:
        pass

    @globaldata_productor(key="rt_arg_getter")
    def provide_runtime_arguments_analysiser_0(self):
        rt_arg_getter = ArgumentAnalysiser(sys.argv)
        return rt_arg_getter

    @globaldata_productor(key="log_service")
    def provide_log_service_1(self):
        log_service = LogService()
        return log_service

    def run__config(self):
        function_orderer = FunctionSort([self])
        function_list = function_orderer.sort()
        for function in function_list:
            function()