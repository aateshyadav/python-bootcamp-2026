# Class : class is a blueprint or a template. Eg. Form for an exam that contains names, age, electives, father's name etc 
# Object : specific instance created from the template (class.). Eg. form which contains the data from john doe

class employee:   # creating a class
    comapny = "HP"
    
    def get_salary(self): # self is important here because self is a way to reference the onbject of the class which is being created 
        return 34000
    
e1 = employee()     # an object of class employee is created here 
print(e1.get_salary())   # employee e's get salary method is called   

e2 = employee()   
print(e2.get_salary()) 
print(e2.comapny)