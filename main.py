
import qrcode

input_data = "my name is xyz"
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,     # defines dimensions of the qr code (LxB)
        error_correction=qrcode.constants.ERROR_CORRECT_H,      # About 30% or fewer errors can be corrected.
        box_size=5,     # defines dimensions of the box that contains QRcode.
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='transparent')
img.save('qrcode001.png')

