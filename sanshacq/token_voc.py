from re import T
import pandas as pd
from tqdm import tqdm
import spacy
from os.path import exists


def get_tokens(nlp, text: str):
    """Get all entities contained in a text.

    Args:
        nlp (SequenceTagger): Flair tagger
        text (str): text to analyze

    Returns:
        List: List with entities.
    """
    doc = nlp(text)

    words = list()
    lemmas = list()
    tags = list()
    for token in doc:
        words.append(token.text)
        lemmas.append(token.lemma_)
        tags.append(token.pos_)

    df = pd.DataFrame(
        columns=[
            "word",
            "lemma",
            "tag",
        ],
        data=zip(words, lemmas, tags),
    )
    return df


def count_pages(n_book, df):
    df_return = pd.DataFrame(columns=["pages", "count"])
    df_return[f"book{n_book}"] = [df.unique()]
    df_return["count"] = df.count()
    return df_return


if __name__ == "__main__":
    """get ners for all boocqs"""

    nlp = spacy.load("en_core_web_sm")
    df_tokens = pd.DataFrame()
    for n_book in tqdm(range(1, 6)):

        path_feather = f"data/allBooqs/SEC450_u{n_book}.feather"
        path_token_feather = path_feather.replace(".", "token.")

        if exists(path_token_feather):
            df_ners = pd.read_feather(path_token_feather).reset_index()
        else:
            df_book = pd.read_feather(path_feather).reset_index()
            df_ners = pd.DataFrame()

            for n, row in tqdm(df_book.iterrows()):
                text = row.text
                df_page = get_tokens(nlp, text)
                df_page["page"] = n + 1
                df_ners = pd.concat([df_ners, df_page], ignore_index=True)
            df_ners.to_feather(path_token_feather)

        tags2keep = ["VERB", "PROPN", "NOUN", "ADJ"]
        print(f"Book {n_book} before filter: ", df_ners.shape)
        df_filter = df_ners.loc[df_ners["tag"].isin(tags2keep)]
        print(f"Book {n_book} after filter: ", df_filter.shape)
        df_lemmas = df_filter.groupby(["lemma"]).apply(
            lambda x: count_pages(n_book, x.page),
        )
        df_lemmas = df_lemmas.reset_index().drop(["level_1"], axis=1)
        df_lemmas = df_lemmas.loc[df_lemmas.lemma.str.len() > 3]
        df_tokens = pd.concat([df_tokens, df_lemmas])

    df_tokens = df_tokens.sort_values(["lemma"])
    df_tokens.groupby(["lemma"])
    df_tokens.sort_values(["count"]).to_csv("./data/SEC450_index_v01.csv")
    print(df_tokens.head())
