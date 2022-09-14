import os
from typing import List
import dotenv
from tqdm import tqdm


def unlocq_sans_books(books: List) -> List:
    """Unlocq Sanshacq books.

    Args:
        books (List): path to the books
    Returns:
        path to unlocked books
    """
    # load_dotenv(find_dotenv())
    dotenv.load()
    BOOQ_PW = dotenv.get("BOOQ_PW")
    print("Double check your pw: ", f"{BOOQ_PW}")
    unlocked = []

    for book_path in tqdm(books):
        unlocked_path = book_path.replace(".pdf", "_unlocked.pdf")
        unlocked.append(unlocked_path)
        os.system(f"qpdf --password=$BOOQ_PW --decrypt {book_path} {unlocked_path}")

    return unlocked


if __name__ == "__main__":
    """Unlock the books"""
    # path_books = "data/allBooqs/SEC450"
    # n = 5
    # unlocq_sans_books(path_books, n)
