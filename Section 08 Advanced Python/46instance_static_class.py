class employee:
    company="HP"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    # Instance method(default)
    def print_info(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    # Static Method
    @staticmethod
    def sum(a,b):
        return a+b
    
    # Class Method
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod     # it is changing the class variable not the instance variable
    def change_company(cls,new_company):
        cls.company=new_company

e1=employee("jack",3455)
e2=employee("jill",4455)

e1.print_info()
e2.print_info()
print(e2.sum(5,23))
e1.print_company()
e1.change_company("Acer")
e1.print_company()
print(employee.company)