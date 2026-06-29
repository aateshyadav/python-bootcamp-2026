# Question : Change tuple to list and then edit value , then again convert list to tuple 
""" tuple_=(10,20)

print(tuple_[0])
print(tuple_[1])

# tuple_[0]=50  # Target value
list_=list(tuple_)
list_[0]=50
tuple_=tuple(list_)
print(tuple_) """

# Question : Write a program that takes a list of numbers and remove all duplicates using a set
""" marks=[1,2,2,3,4,5,5]
print(marks)
set_=set(marks)
print(set_) """

# Question : Find highest priced product in a dictionary
""" products={"ball":50,"bat":200,"wickets":100}
print(products.values())
print(products.keys())
highest_product=max(products,key = products.get)
highest_price=products[highest_product]
print(highest_product,highest_price) """

# Question : Write a program that merges two dictionaries into one
dict1={"ball":50,"bat":200,"wickets":100}
dict2={"screen":2000,"speaker":1000,"mic":500}

dict1.update(dict2)     # Method 1
print(dict1)

merged=dict1 | dict2    # Method 2 
print(merged)