"""
Generate qr code for a given information.
"""

import qrcode 

# data k halne ta???
data = "https://github.com/masabinhok/python-for-automation"

# file path for saving qr code

output_file = 'qrcode.png'

# qr code function le chai dherai argument linxa, version to specify the size, error correction method, size of each box in px, border size in boxes..


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# qr ma data add garna paryo
qr.add_data(data)
qr.make(fit=True)

# img banaunu paryo from the qr code instance
img = qr.make_image(fill_color="red", back_color="white")

# img save garne, 
img.save(output_file)

print("qr code generated")
