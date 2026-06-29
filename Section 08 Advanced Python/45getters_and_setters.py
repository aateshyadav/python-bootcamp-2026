class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

# first_name = first + second
    @property
    def first_name(self):   # splitting first_name and count only first word
        l = self.name.split(" ")  
        return l[0]         # returning only first part of first_name
    
    @first_name.setter
    def first_name(self, first):    # extracting first word
        l=self.name.split(" ")      # splitted in two parts
        new_name=f"{first} {l[1]}"  # new_name=first and second remain same 
        self.name=new_name

e=employee("jack doe",34555)  # input first_name and salary

print(e.first_name)  
e.first_name="john"  # putting self = john
print(e.name) 

