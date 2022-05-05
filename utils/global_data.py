import inspect
class GlobalData:
    data = {}
    def __init__(self) -> None:
        pass

    @staticmethod
    def set_status(key,value):
        GlobalData.data[key] = value

    @staticmethod
    def get_status(key):
        return GlobalData.data[key]
    
    @staticmethod
    def contains(key):
        return key in GlobalData.data

def globaldata_productor(key):
    def agenter(fn):
        def new_functions(*args,**kwords):
            result = fn(*args,**kwords)
            GlobalData.set_status(key=key,value=result)
            return result
        return new_functions
    return agenter

def auto_wired(fn):
    sig_args = [arg for arg in inspect.signature(fn).parameters if arg != 'self']
    def new_functions(*args,**kwords):
        for arg in sig_args:
            if arg not in kwords and GlobalData.contains(key=arg):
                kwords[arg] = GlobalData.get_status(arg)
        return fn(*args,**kwords)
    return new_functions