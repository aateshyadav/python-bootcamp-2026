# inheritance ]
class animal:
    location="australia"
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("speaking now...")

class dog(animal):  #this is how inheritance is done in python 
    def speak(self):
        super().speak()   # getting instance of parent class and calling its methods
        print("woof!")

""" a=animal("dog")
a.speak() """
d=dog("bruno")
d.speak()
print(d.location)

