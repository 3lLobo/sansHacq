# Indexing Info in Sans-books

```
Disclaimer: This repo is experimental and not liable for any damage or misuse, neither is it linked to any person, company or public entity.
```

Use this repo to automatically generate an word/entity index of the class-books in order to prepare for the exam.

## How to use

1. Drop your pdf files in `data/allBooqs/*`
1. Use the naming convention ```<course_name>_<book_number>.pdf``` wiht numbers starting from 1.
3. Run 🏃🏾‍♂️ the script.
4. A csv file wih the index should appear in `data/index_<course_name>.csv`.
5. STUDY!!!

Install and execute (with Poetry package manager):
```sh
poetry install
poetry run python run.py --course_name <> --n_books <>

```

### ner-tagging

If you are interested in Named Entity recognition, feel free to play around in `sanshacq/ner_tagging.py`.
It will generate a html file with colored entities.

### TF-IDF score

Run `sanshacq/n_gram.py` to have a look into the tf-idf score of the documents.

## Open TODOs

Index:

-   Join index table with Tdf-Idf score table
-   Filter based  on score
-   n-gram

## Spacy hacqs

Get the full vocab:

```py
list(nlp.vocab.strings)
```

[Source of inspiration](https://www.dataquest.io/blog/tutorial-text-classification-in-python-using-spacy/)
