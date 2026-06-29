class employee:
    company="Asus"  # This is class attribute

    def __init__(self,  salary, name, bond,company):   # Constructor in action
        self.salary=salary   
        self.name=name
        self.bond=bond
        self.company=company

    def get_salary(self):
        return self.get_salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}.\nSalary is {self.salary}.\nThe bond is for {self.bond} years.")

e1 = employee(34000,"John",3,"Tesla")
print(e1.company)  # will always print instance attribute whenever present
print(employee.company)   # this will always print the class attribute

# Object introspection
print(dir(e1))           