#  inspiration: https://learndataanalysis.org/how-to-extract-text-from-a-pdf-file-using-python/
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import tika
import pprint
import pdfplumber
import pandas as pd
from tqdm import tqdm


def extract_text_plumber(pdf_path: str) -> pd.DataFrame:
    """Extract text from a pdf and return a table with page number and text.

    Args:
        pdf_path (str): path to the Pdf
    Returns:
        pd.DataFrame: extracted data
    """

    df = pd.DataFrame(columns=["page", "text"])
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # add to df
            df = pd.concat(
                [
                    df,
                    pd.DataFrame.from_dict(
                        {
                            "page": [page.page_number],
                            "text": page.extract_text().replace("\n", " "),
                        }
                    ),
                ],
                ignore_index=True,
            )
    df.to_feather(pdf_path.replace(".pdf", ".feather"))
    return df


def extract_text_tika(pdf_path: str):
    """Extract text from a pdf and save as text file per page.

    Args:
        pdf_path (str): path to the Pdf
    """
    tika.initVM()
    from tika import parser

    folder_path = pdf_path.split(".")[0]
    os.makedirs(folder_path, exist_ok=True)

    parsed = parser.from_file(
        pdf_path,
    )
    content = parsed["content"]
    print(parsed["metadata"])
    print(parsed["content"])


if __name__ == "__main__":
    """Extract text from pdf books"""

    for n in tqdm(range(5)):
        pdf1 = f"data/allBooqs/SEC450_u{n+1}.pdf"
        df = extract_text_plumber(pdf1)
        pprint.pprint(df.head())
