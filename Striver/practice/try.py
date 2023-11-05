class Employee:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def _show(self):
        print(self._name,self._age)

e1 = Employee("bony",26)
e1.show()