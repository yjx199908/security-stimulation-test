from array import array

class FunctionSort:
    def __init__(self,instances:array) -> None:
        self.instances = instances
    
    def get_function_keys(self,instance):
        class_name = '_{}'.format(type(instance).__name__)
        function_keys = [key for key in dir(instance) if not key.startswith('__') and not key.startswith(class_name) and not key.startswith('run__')]
        function_keys.sort(key=lambda key:int(key.split('_')[-1]))
        return function_keys

    def sort(self):
        instances = self.instances
        function_list = []
        for instance in instances:
            function_keys = self.get_function_keys(instance)
            function_list.extend([getattr(instance,item) for item in function_keys])
        return function_list