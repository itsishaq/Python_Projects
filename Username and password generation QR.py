import pyqrcode
import cv2
from pyzbar.pyzbar import decode
from PIL import Image

print("**) Press 1 for account creation \n**) Press 2 for ticketing")
a=int(input())
d=100000000000
if(a==1):
    file= open("Qr_code_username_password.txt", "a+")
    fname=input("enter you name::")
    file.write(fname)
    d+=file.tell()
    file.write(str(d)+'\n')
    fwallet=input("enter the wallet money::")
    file.write(fwallet +'\n')
    #close file
    file.close()
if(a==2):
    print("Enter the decode qr")
    a = input()
    file = open("Qr_code_username_password.txt", "r")
    if (a in file.read()):
        qr_code = pyqrcode.create(file.read())
        qr_code.png("QrCodesample234.png", scale=10)
        print("Valid")
    else:
        print("Invalid")
