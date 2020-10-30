class computor:

    def __init__(self,cpu,ram):
        self.cpu= cpu
        self.ram = ram

    def config(self):
        print("this sytem configure is: ",self.cpu,self.ram,"windows7")

com1 = computor('i5',16)
com2 = computor('i6',32)


com1.config()
com2.config()
