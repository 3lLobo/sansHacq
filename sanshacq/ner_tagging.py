# https://huggingface.co/flair/ner-english-large?text=George+Washington+went+to+Washington
# https://medium.com/quantrium-tech/top-3-packages-for-named-entity-recognition-e9e14f6f0a2a

from typing import List
from flair.data import Sentence
from flair.models import SequenceTagger
import pandas as pd
from tqdm import tqdm

# load tagger
# tagger = SequenceTagger.load("flair/ner-english-large")


def get_ners(tagger: SequenceTagger, text: str) -> List:
    """Get all entities contained in a text.

    Args:
        tagger (SequenceTagger): Flair tagger
        text (str): text to analyze

    Returns:
        List: Lit with entities.
    """
    # make example sentence
    sentence = Sentence(text)
    # predict NER tags
    tagger.predict(sentence)
    # print sentence
    print(sentence)

    # print predicted NER spans
    print("The following NER tags are found:")
    # iterate over entities and print
    df = pd.DataFrame(columns=["text", "tag"])
    for entity in sentence.get_spans("ner"):
        print(entity)
        df_ent = pd.DataFrame(columns=["text", "tag"], data=[[entity.text, entity.tag]])
        df = pd.concat([df, df_ent])

    return df


if __name__ == "__main__":
    """get ners fro all boocqs"""
    path_feather = "data/allBooqs/SEC450_u1.feather"
    tagger = SequenceTagger.load("ner")

    df_book = pd.read_feather(path_feather)

    df_ners = pd.DataFrame(columns=["text", "tag", "page"])
    # df["ners"] = df.apply(
    #     lambda x: get_ners(tagger, text[0]),
    #     result_type="reduce",
    # )
    for n in tqdm(range(len(df_book))):

        text = df_book.loc[n, ["text"]][0]
        df_page = get_ners(tagger, text)
        df_page["page"] = n + 1
        df_ners = pd.concat([df_ners, df_page])
        print(df_ners.head())

    df_ners.to_feather(path_feather.replace(".", "ners."))
