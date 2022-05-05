from array import array
import pathlib
import os
from datetime import datetime
class LogService:
    def __init__(self) -> None:
        self.common_log_cache = []
        self.error_log_cache = []
        self.prepare_log_conditions()

    def prepare_log_conditions(self):
        path = pathlib.Path("dong-test-sys")
        print(path.absolute())
        if not path.exists():
            path.mkdir()

    def get_target_array(self,kind):
        if kind == 'common':
            return self.common_log_cache
        elif kind == 'error':
            return self.error_log_cache

    # kind: common|error
    def write_log_into_files(self,kind):  
        file_name = './dong-test-sys/{}-{}.log'.format(datetime.now().strftime("%Y-%m-%d"),kind)
        path = pathlib.Path(file_name)
        if not path.exists():
            path.touch()
        target_cache:array = self.get_target_array(kind=kind)
        with open(file=file_name,encoding="utf-8",mode="a") as fp:
            fp.writelines(target_cache)
            target_cache.clear()
        
    def log(self,kind,content):
        target_cache = self.get_target_array(kind)
        log_content = '[{}]{} - {}\n'.format(str.upper(kind),datetime.now().strftime("%Y-%m-%d %H:%M:%S"),content)
        print(log_content)
        target_cache.append(log_content)
        self.write_log_into_files(kind)