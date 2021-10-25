#Import the following packages -(pyqrcode, pillow, pyzbar, pypng)

import pyqrcode

from pyzbar.pyzbar import decode

from PIL import Image

qr_code = pyqrcode.create("Hey bro wanna know my wifi password..??")

#Any context can be given as input for generating the QR code as you like

qr_code.png("QrCode.png",scale=10)

print("QR-Code generation is Completed.!")
