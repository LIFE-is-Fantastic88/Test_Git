import qrcode

# Define the data to encode in the QR code
data = "Hello, my little girl esther. Today is Friyay. Book your Sat and Sun pi happy ya. This sat we pi gurney paragon, onz mou?"  # Replace this with your desired data

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
qr_image.save("qrcode.png")