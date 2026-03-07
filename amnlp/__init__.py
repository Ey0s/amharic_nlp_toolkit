from .tokenizer.tokenizer import AmharicTokenizer
from .stemmer.stemmer import AmharicStemmer
from .stopwords.stopwords import StopwordRemover
from .normalization.normalizer import AmharicNormalizer
from .pipeline.processor import AmharicProcessor

def tokenize(text):
    return AmharicTokenizer().tokenize(text)

def stem(tokens):
    return AmharicStemmer().stem(tokens)

def remove_stopwords(tokens):
    return StopwordRemover().remove(tokens)