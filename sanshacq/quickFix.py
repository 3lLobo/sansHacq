import pandas as pd


df = pd.read_csv("./data/SEC450_index_v01.csv")

# df = df.sort_values(['lemma'])

# df.groupby(['lemma'])

# TODO: groupby lemma

# TODO: drop cols book ...

# TODO: find typos ✅


df.to_csv("./data/SEC450_index_v01_asc.csv")
