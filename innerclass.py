class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpe = 'i5'
            self.ram = '32'

        def show(self):
            print(self.brand,self.cpe,self.ram)


s1 = Student('anji',3)
s2 = Student('thanu',5)

s1.show()
s2.show()
