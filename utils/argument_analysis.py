from array import array
default_args = {
    "--interval":300
}
class ArgumentAnalysiser:
    def __init__(self,argv) -> None:
        self.set_args(argv=argv)
        pass
    
    def set_args(self,argv) -> None:
        args = argv[1:]
        arg_map = default_args.copy()
        for arg in args:
            if arg.find('=') == -1:
                continue
            [key,value] = arg.split('=')
            arg_map[key] = value
        self.arg_map = arg_map
    
    def get(self,key:str):
        if key not in self.arg_map:
            return None
        return self.arg_map[key]