# singleton -- one single instance 

class Singleton:
    _instance = None
    def __init__(self) -> None:
        if Singleton._instance is None:
            Singleton._instance = self 
        else:
            raise Exception('This is single')
        
    @staticmethod
    def get_instence():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

first = Singleton.get_instence()
print(first)