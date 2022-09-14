import argparse

import pandas as pd
from sanshacq.pdf2text import extract_all

from sanshacq.token_voc import get_full_index
from sanshacq.unlocq_books import unlocq_sans_books

parser = argparse.ArgumentParser(
    description="Index your school books and enrich with tdl-idf score.",
    epilog="Arguments indicate name convention and count of books. \nPlease place the books in /data/allBooqs and follow this naming convention (book_number starting at 1): <course_name>_<book_number>.pdf \n Create a .env file and place the password to unlock the books as shown in .env.example.",
)

parser.add_argument(
    "--course_name", dest="course_name", type=str, help="Name of the course"
)
parser.add_argument("--n_books", dest="n_books", type=int, help="Number of books")
parser.add_argument(
    "--no_pw", dest="no_pw", type=bool, help="Books do not require a password"
)

args = parser.parse_args()

# create book path
books = []

for n in range(args.n_books):
    path = "data/allBooqs/{}_{}.pdf".format(args.course_name, n + 1)
    books.append(path)

# unlock books
if args.no_pw:
    pass
else:
    print("\nUnlocking books...")
    books = unlocq_sans_books(books)
    print("Success unlocking books!")

# extract text from pdf
print("\nExtracting text from pdf...")
extract_all(books)
print("Success text extraction!")

# index books
print("\nStart indexing books...")
df_index = get_full_index(books)
index_path = "data/index_{}.csv".format(args.course_name)
df_index.to_csv(index_path)
print("\nSuccess creating index! \nStored in: ", index_path)

# TODO: add tdl-idf score
