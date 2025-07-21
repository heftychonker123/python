from abc import ABC,abstractmethod
class chonky(ABC):
    @abstractmethod
    def rub(self):
        pass
class dog(chonky):
    def rub(self):
        print("You rub the belly of a chonky dog")
dog=dog()
dog.rub()