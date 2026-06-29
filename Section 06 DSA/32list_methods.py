""" marks=[5,2,21,5,7]
extra_marks=[1,2,3]

print(marks)

marks.append(63)  #adding 63 at the end of list
print(marks)
marks.pop()
print(marks)

marks.extend(extra_marks) #it will add extra_marks list to the marks list
print(marks)

marks.reverse()
print(marks)

marks.sort()
print(marks)

 """

#List Comprehension
#create a list containing list of five 
#a=5
""" table=[]
for i in range(1,11):
    table.append(5*i)
 """

table=[5*i for i in range(1,11)]
print(table)