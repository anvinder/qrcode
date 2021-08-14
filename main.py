import qrcode
import PyPDF2
from MyQR import myqr as mq

pdfFile = open('qrco.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('password')
resultPdf = open('encrypted_output.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()

#input_data = resultPdf
input_data = 'asd.jpg'
qr = qrcode.QRCode(
        version=5,                                              # defines dimensions of the qr code (LxB)
        error_correction=qrcode.constants.ERROR_CORRECT_H,      # About 30% or fewer errors can be corrected.
        box_size=5,                                             # defines dimensions of the box that contains QRcode
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode.png')
