# Read a file
""" f=open("53.1files.txt","r")

content=f.read()

print(content)

f.close() """




# Write a file
""" f = open("53.2john doe.txt","w")   # making file name

#file text
string='''  
John doe  is a nice guy.he lives in nyc and he works with python
His favourite package is pandas
'''

f.write(string)   #writing text in file

f.close() """




# Append in a file; addding data to the end of file
""" f = open("53.2john doe.txt","a")

string='''  
John Doe initially lived in phoenix,arizona. he is very nice guy
'''

f.write(string)

f.close() """




# Read file line by line
""" f=open("53.1files.txt","r")

for line  in f:
    print(line)

f.close() """




# Read by using with
with open("53.1files.txt","r") as f:
    content = f.read()
    print(content)
    # No need to write f.close() becausere file is already closed by default when using with syntax 