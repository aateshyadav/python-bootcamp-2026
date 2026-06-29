""" str="  i love python programming  "
# print(str.strip())
# .title  to make title out of text
# .count("o")  to count number of o letters in text
count=0
v = ("a", "e", "i", "o", "u")
for char in str.lower():
    if char in v:
        count += 1
print("Number of vowels:", count) """

string="madam"
if (string == string[::-1]):
    print("it is a pallindrome")
else:
    print("not a pallindrome")
