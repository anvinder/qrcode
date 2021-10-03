import os
from os import listdir
from os.path import isfile, join
import PyPDF2
import qrcode

class QrCode:
    def __init__(self):
        self.mypath = os.getcwd()
        self.syncpath = "C:\\Users\\anvin\\Sync"
        self.file_list = []
        self.pdf_file_list = []
        self.encrypted_file_list = []
        self.dictionary_items = {}

    def File_list(self):
        for f in listdir(self.mypath):
            if isfile(join(self.mypath,f)):
                self.file_list = self.file_list + [f]
        self.encrypt_file(self.file_list)

    def encrypt_file(self, file_list):
        for item in self.file_list:
            if item.endswith('.pdf') and 'encrypt' not in item:
                self.pdf_file_list += [item]
        print(self.pdf_file_list)
        for item in self.pdf_file_list:
            pdfFile = open(item, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            pdfWriter.encrypt('abcd')
            resultPdf = open(item + '_encrypt.pdf', 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()

    def dict_items(self):

        for file in listdir(self.syncpath):
            if isfile(join(self.syncpath, file)):
                self.encrypted_file_list = self.encrypted_file_list + [file]
        self.dictionary_items.update\
        (
            {
			'Apy':'www.google.com'
			'crap' : 'www.amazon.com'
			}
        )

    def gen_qrcode(self):
        for key, val in self.dictionary_items.items():
            qr = qrcode.QRCode(
                version=2,  # defines dimensions of the qr code (LxB)
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # About 30% or fewer errors can be corrected.
                box_size=1,  # defines dimensions of the box that contains QRcode
                border=5)
            qr.add_data(val)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save(key+'.jpg')


if __name__ == "__main__":
    object_qrcode = QrCode()
    object_qrcode.File_list()
    object_qrcode.dict_items()
    object_qrcode.gen_qrcode()

	
