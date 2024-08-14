import random
import nltk
from nltk.corpus import wordnet

# Download necessary NLTK data
nltk.download('wordnet')

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().replace('_', ' '))
    return list(synonyms)

def create_variations(sentence, num_variations=25):
    words = sentence.split()
    variations = []
    for _ in range(num_variations):
        new_sentence = []
        for word in words:
            synonyms = get_synonyms(word)
            if synonyms and random.random() > 0.5:
                new_sentence.append(random.choice(synonyms))
            else:
                new_sentence.append(word)
        variations.append(' '.join(new_sentence))
    return variations