# https://huggingface.co/flair/ner-english-large?text=George+Washington+went+to+Washington
# https://medium.com/quantrium-tech/top-3-packages-for-named-entity-recognition-e9e14f6f0a2a

from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("flair/ner-english-large")

# make example sentence
sentence = Sentence("George Washington went to Washington")

# predict NER tags
tagger.predict(sentence)

# print sentence
print(sentence)

# print predicted NER spans
print('The following NER tags are found:')
# iterate over entities and print
for entity in sentence.get_spans('ner'):
    print(entity)