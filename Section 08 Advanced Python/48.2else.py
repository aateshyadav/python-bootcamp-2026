#else
try:
    a=345/0

except Exception as e:
    print(e)

# Gets executed when there is no error in the try block
else:
    print("hey i am good")
