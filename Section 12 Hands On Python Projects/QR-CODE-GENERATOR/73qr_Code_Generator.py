'''
we are going to use a python library like qrcode to convert url to qr
'''
import qrcode 

url = input("Enter your QR: ")
filename=input("Filename you want to save it as: ")
if not(filename.endswith(".png")):
    filename=filename+".png"

img=qrcode.make(url)
img.save(filename)