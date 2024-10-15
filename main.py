import os
# from os.path import isfile
from PyPDF2 import PdfReader, PdfWriter
import argparse
from helpers import create_basePaths


SRC_DIR = os.path.dirname(os.path.abspath(__file__))

def main(file_path:str):
    print(f"File path: {file_path}")
    filename_w_ext = os.path.basename(file_path)
    baseFilename = os.path.splitext(filename_w_ext)[0]
    baseFilenameExt = os.path.splitext(filename_w_ext)[1]
    print(f'File name: {filename_w_ext} |basefilename: {baseFilename} | baseFilenameExt : {baseFilenameExt}')
    print(f"src path:{SRC_DIR}")
    destFilePath = os.path.join(SRC_DIR, f'dest/{baseFilename}')
    print(f"Destination file path: {destFilePath}")
    if not os.path.exists(destFilePath):
        os.makedirs(destFilePath)
    
    pdfReader = PdfReader(file_path)
    for page_num in range(len(pdfReader.pages)):
        pdfWriter = PdfWriter()
        pdfWriter.add_page(pdfReader.pages[page_num])
        output_pdf_path = os.path.join(destFilePath, f"{baseFilename}_page_{page_num + 1}.pdf")
        with open(output_pdf_path, 'wb') as output_pdf_file:
            pdfWriter.write(output_pdf_file)

if __name__ == '__main__':
    create_basePaths()
    parser = argparse.ArgumentParser(description="PDF Splitter")
    parser.add_argument("file_path", help="File path of pdf to split")
    args = parser.parse_args()
    _path = args.file_path
    if os.path.isfile(_path):
        print("File Path Given")
    else:
        print("Folder path given")
    main(args.file_path)
