""" name="aatesh"  # string are imutable
a=len(name)
print(a) """



""" s="hello world"
a=len(s)
print(a)
print(s.upper())
print(s)
print(s.capitalize())
print(s.title()) """


""" text="  hello world  "
print(text.strip())
print(text.lstrip())
print(text.rstrip())  """


""" text="python is fun and fun and fun"
print(text.find("is"))
print(text.replace("fun","awesome"))
 """


""" text="Apples,Bananas,Pineapples"
print(text.split(","))
print(",".join(['mango','kiwi','litchi']))
 """


""" text="python123"
print(text.isalpha()) #False
print(text.isdigit()) #False
print(text.isalnum()) #True
print(text.isspace()) #False """


template="dear {}, you are awesome. take this {}$ bag"
a="john"
a1=10000
b="jack"
b1=1000
c="marry"
c1=300
s1=template.format(a,a1)   #format function
print(s1)
print(f"dear {b}, you are awesome. take this {b1}$ bag")  # string function
