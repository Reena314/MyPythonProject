import qrcode

data = input("Enter the text or URL: ").strip()
fileName = input("Enter the filename (with .png): ").strip()

# Initialize QRCode with proper keyword arguments
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(data)           # correct method name
qr.make(fit=True)           # generate the QR code

# Create the image
img = qr.make_image(fill_color="black", back_color="white")
img.save(fileName)

print(f'QR code saved as {fileName}')
               
               # important

# pip install qrcode  
# after this code use pip3 install pillow
# and then run
#  