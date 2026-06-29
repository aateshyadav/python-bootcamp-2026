class employee:

    def __init__(self,  salary, name, bond):   # Constructor in action
        self.salary=salary
        self.name=name
        self.bond=bond

    def get_salary(self):
        return self.get_salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}.\nSalary is {self.salary}.\nThe bond is for {self.bond} years.")

e1=employee(34000,"John Doe",4)
e1.get_info()
