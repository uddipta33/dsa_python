

class Employee:
    raise_amount = 5000 #class variable

    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "." + last + "@gmail.com"
    
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    def raise_salary(self):
        self.salary = self.salary+Employee.raise_amount

class Developer(Employee):
    def __init__(self,first,last, salary, prog_lang):
        super().__init__(first,last,salary)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last, salary, emps=None):
        super().__init__(first,last, salary)
        if emps is None:
             self.emps = []
        else:
            self.emps = emps
    
    def add_emps(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)
    
    def remove_emps(self,emp):
        if emp in self.emps:
            self.emps.remove(emp)
    def print_emps(self):
        for emp in self.emps:
            print("---->",emp.fullname())

dev1 = Developer("Ram","Gopal",50000,"Java")
dev2 = Developer("Ved","Sarma",70000,"Golang")
print(dev1.fullname())
print(dev1.email)
dev1.raise_salary()
print(dev1.salary)

mng1 = Manager("Dev","Das",90000,[dev1])
# mng1.print_emps()
mng1.add_emps(dev2)
mng1.print_emps()