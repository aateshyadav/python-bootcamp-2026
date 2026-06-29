import math
import os
import requests

print(math.sqrt(16))

r = requests.get("https://www.google.com")
print(r.text)   # .text to fetch html file of the link written
