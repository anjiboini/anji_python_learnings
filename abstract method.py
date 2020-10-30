from abc import ABC,abstractmethod

class computor(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computor):
    def process(self):
        print("it is running")

com1 = laptop()
com1.process()