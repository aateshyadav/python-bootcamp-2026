""" s={3,23,2,11}   # Sets can't have duplicate elements

print(s,type(s))
 # print(s[3]) #You are not allowed to something like this 

s.add(22)
print(s)
s.remove(2)
print(s) """


# Operations
a={3,23,1}
b={23,4,2,55,1}

c=a.union(b)
print(c)

d=a.intersection(b)
print(d)

e=a-b
print(e)
