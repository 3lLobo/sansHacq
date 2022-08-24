# Do ngram on the whole document or each page.
import string
from typing import List
import pandas as pd
import spacy
import contextualSpellCheck
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Create our list of punctuation marks
punctuations = string.punctuation

# Create our list of stopwords
stop_words = spacy.lang.en.stop_words.STOP_WORDS

nlp = spacy.load("en_core_web_sm")
# Create the pipeline 'sentencizer' component
nlp.add_pipe("sentencizer")

contextualSpellCheck.add_to_pipe(nlp)


# Creating our tokenizer function
def spacy_tokenizer(sentence):
    # Creating our token object, which is used to create documents with linguistic annotations.
    mytokens = nlp(sentence)
    page = spacy.displacy.render(mytokens, style="ent", jupyter=False)
    with open("./spacy.html", "w") as f:
        f.write(page)

    # Lemmatizing each token and converting each token into lowercase
    mytokens = [
        word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_
        for word in mytokens
    ]

    # Removing stop words
    mytokens = [
        word for word in mytokens if word not in stop_words and word not in punctuations
    ]

    # Filter short words
    mytokens = [word for word in mytokens if len(word) > 2]

    # return preprocessed list of tokens
    return mytokens


def n_gram(booqs: List, n=1):
    """Input Text, return n-grams.

    Args:
        booq (List): List of full text string objects.
        n (int, optional): order of grams. Defaults to 1.
    Returns:
        matrix: tfidf-matrix
        vectorizer: vectorizer
    """
    # bow_vector = CountVectorizer(tokenizer=spacy_tokenizer, ngram_range=(1, n))
    tfidf_vector = TfidfVectorizer(
        tokenizer=spacy_tokenizer, strip_accents="ascii", ngram_range=(1, n)
    )

    dc_matrix = tfidf_vector.fit_transform([booq])

    return dc_matrix, tfidf_vector


# Basic function to clean the text
def clean_text(text):
    # Removing spaces and converting text into lowercase
    return text.strip().lower()


def correct_typos(text: str) -> str:
    """Correct typos in text.
    Source: https://spacy.io/universe/project/contextualSpellCheck

    Args:
        text (str): text to correct

    Returns:
        str: corrected text
    """
    doc = nlp(text)
    print("Performed spell check? ", doc._.performed_spellCheck)
    if doc._.performed_spellCheck:
        return doc._.outcome_spellCheck
    else:
        return text


if __name__ == "__main__":
    """Test n_gram."""
    path_feather = "data/allBooqs/SEC450_u1.feather"
    df_book = pd.read_feather(path_feather)

    booq = df_book["text"].str.cat(sep=" ")[1000:20000]
    booq = clean_text(booq)
    booq = correct_typos(booq)

    tokens = spacy_tokenizer(booq)

    doc_matrix, tfidf_vector = n_gram(booq, n=2)
    doc_voc = tfidf_vector.get_feature_names_out()
    doc_voc[doc_matrix.argmax(axis=1)]
