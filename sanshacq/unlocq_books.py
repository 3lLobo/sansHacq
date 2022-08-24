import os
import dotenv
from tqdm import tqdm


def unlocq_sans_books(path_books: str, n_books: int):
    """Unlocq Sanshacq books.

    Args:
        path_books (str): path to the books
        n_books (int): number of books
    """
    # load_dotenv(find_dotenv())
    dotenv.load()
    BOOQ_PW = dotenv.get("BOOQ_PW")
    print("Double check your pw: ", f"{BOOQ_PW}")

    for n in tqdm(range(n_books)):
        os.system(
            f"qpdf --password=$BOOQ_PW --decrypt {path_books}_{n+1}.pdf {path_books}_u{n+1}.pdf"
        )


if __name__ == "__main__":
    """Unlock the books"""
    path_books = "data/allBooqs/SEC450"
    n = 5
    unlocq_sans_books(path_books, n)
