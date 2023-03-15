# coding: utf-8

import PyPDF2
import glob
import os

def merge_pdf_in_dir(dir_path, dst_path):
    l = glob.glob(os.path.join(dir_path, '*.pdf'))
    l.sort()

    merger = PyPDF2.PdfMerger()
    for p in l:
        if not PyPDF2.PdfReader(p).is_encrypted:
            merger.append(p)

    merger.write(dst_path)
    merger.close()

print("PDFmerger.exeと同じ階層にあるPDFファイルを結合して、Outputフォルダに出力しようとしています。")
name = input("出力するファイル名を入力してください：")

dir_path = "output"
os.makedirs(dir_path, exist_ok=True)
merge_pdf_in_dir('.', f'output/{name}.pdf')

