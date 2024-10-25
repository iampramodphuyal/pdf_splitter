from typing import Annotated, Optional
from pandas.core.series import base
import pdfplumber
import pandas as pd
import os
ROOT_DIR = os.getcwd()
FILE_PATH = os.path.join(str(ROOT_DIR), 'src.pdf')
def convert(filepath:str, filename:Annotated[Optional[str], "The base file name"]=None):
    fpath = filepath if filepath else FILE_PATH
    fname = filename if filename else os.path.splitext(os.path.basename(filepath))[0]
    basedir = os.path.dirname(fpath)
    print(f"csv file path: {fpath} <> filename: {fname} <> basedir:  {basedir}")
    with pdfplumber.open(fpath) as f:
        firstpage = f.pages[0]
        tables = firstpage.extract_tables()

    csv_files = []
    for i, table in enumerate(tables):
        df = pd.DataFrame(table)
        csvfile = f'{ROOT_DIR}/dest/{fname}/extracted_table_{i+1}.csv'
        csvfile = f"{basedir}/{fname}_table_{i+1}.csv"
        df.to_csv(csvfile, index=False, header=False)
        csv_files.append(csvfile)
    totalCsvProcessed = len(csv_files)
    print(f"Total file processed: {totalCsvProcessed}")
