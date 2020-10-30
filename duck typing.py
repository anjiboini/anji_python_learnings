class Pycharm:
    def execute(selfs):
        print("Compilling")
        print("Running")

class Myeditor:
    def execute(selfs):
        print("Spell checking")
        print("convention check")
        print("Compilling")
        print("Running")

class laptop:
    def code(self,ide):
        ide.execute()

ide = Pycharm()
#or
#ide = Myeditor

lap1 = laptop()
lap1.code(ide)