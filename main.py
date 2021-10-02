import os
from os import listdir
from os.path import isfile, join
import PyPDF2

class qrcode:
    def __init__(self):
        self.mypath = os.getcwd()
        self.file_list = []
        self.pdf_file_list = []
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
            pdfWriter.encrypt('password')
            resultPdf = open(item + '_encrypt.pdf', 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()


if __name__ == "__main__":
    object_qrcode = qrcode()
    object_qrcode.File_list()
