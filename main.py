import os
from typing import Optional
# from os.path import isfile
from PyPDF2 import PdfReader, PdfWriter
import argparse
from helpers import create_basePaths
from pdf2csv import *

SRC_DIR = os.path.dirname(os.path.abspath(__file__))

def main(file_path:str, _export:Optional[str]):
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
        print(f"Output pdf path:{output_pdf_path}")
        with open(output_pdf_path, 'wb') as output_pdf_file:
            pdfWriter.write(output_pdf_file)
        if _export:
            convert(output_pdf_path)

if __name__ == '__main__':
    create_basePaths()
    parser = argparse.ArgumentParser(description="PDF Splitter")
    parser.add_argument("file_path", help="File path of pdf to split")
    parser.add_argument('-p', help="Number of page to process, can be like 1,2,3 or 1-3")
    parser.add_argument('-e','--export',action="store_true", help="Add this flag to export processed pages to csv")
    args = parser.parse_args()
    _isExport = args.export
    _path = args.file_path
    if os.path.isfile(_path):
        print("File Path Given")
        main(args.file_path,_isExport)
    else:
        print("Folder path given")
        # pdfLists = [f for f in os.listdir(_path) if f.endswith(".pdf")]
        for file in os.listdir(_path):
            if file.endswith(".pdf"):
                main(file, _isExport)
