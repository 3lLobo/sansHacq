# Indexing Info in Sans-books

```
Disclaimer: This repo is experimental and not liable for any damage or misuse, neither is it linked to any person, company or public entity.
```

Use this repo to automatically generate an word/entity index of the class-books in order to prepare for the exam.

## How to use

1. Drop your pdf files in `data/allBooqs/*`
2. Adjust the file-names and count in `sanshacq/unlocq_books.py`.
3. Run `/sanshacq/token_voc.py`.
4. A csv file wih the index should be visible in `data/`.
5. STUDY!!!

### ner-tagging

If you are interested in Named Entity recognition, feel free to play around in `sanshacq/ner_tagging.py`.
It will generate a html file with colored entities.

### TF-IDF score

Run `sanshacq/n_gram.py` to have a look into the tf-idf score of the documents.

## Open TODOs

Index:

-   keywords
-   n-gram
-   Stop words:

## Spacy hacqs

Get the full vocab:

```py
list(nlp.vocab.strings)
```

[Source of inspiration](https://www.dataquest.io/blog/tutorial-text-classification-in-python-using-spacy/)
