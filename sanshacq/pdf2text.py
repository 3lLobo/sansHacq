#  inspiration: https://learndataanalysis.org/how-to-extract-text-from-a-pdf-file-using-python/
from PyPDF2 import PdfFileReader, PdfFileWriter
import os


file_path = 'Lecture.pdf'

def extract_text(pdf_path: str):
    """Extract text from a pdf and save as text file per page.

    Args:
        pdf_path (str): path to the Pdf
    """
    os.makedirs(pdf_path.split('.')[0], exist_ok=True)

    pdf = PdfFileReader(file_path)
    for page_num in range(pdf.numPages):
        with open(f'{page_num}.txt', 'w') as f:
        # print('Page: {0}'.format(page_num))
        pageObj = pdf.getPage(page_num)

        try: 
            txt = pageObj.extractText()
            print('Page {0}\n'.format(page_num+1))
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100, '-'))
            f.write(txt)
        f.close()
