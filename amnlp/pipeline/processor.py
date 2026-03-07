from amnlp.tokenizer.tokenizer import AmharicTokenizer
from amnlp.normalization.normalizer import AmharicNormalizer
from amnlp.stopwords.stopwords import StopwordRemover
from amnlp.stemmer.stemmer import AmharicStemmer
import regex as re

PREFIXES = ["በ", "ከ", "ለ", "ወደ", "የ", "እየ", "እንደ", "በስተ", "በት"]

def split_prefix(word):
    """
    Split common Amharic prefixes from a word.
    Example: በትምህርት -> ['በ', 'ትምህርት']
    Only split if the remaining token is at least 2 characters.
    """
    for prefix in PREFIXES:
        if word.startswith(prefix) and len(word) > len(prefix) + 2:
            return [prefix, word[len(prefix):]]
    return [word]

def split_tokens(tokens):
    """Apply prefix splitting to a list of tokens"""
    result = []
    for token in tokens:
        result.extend(split_prefix(token))
    return result

class AmharicProcessor:

    def __init__(self):
        self.normalizer = AmharicNormalizer()
        self.tokenizer = AmharicTokenizer()
        self.stopwords = StopwordRemover()
        self.stemmer = AmharicStemmer()

    def process(self, text, return_structure=False):
        """
        Process Amharic text with a full NLP pipeline.
        Steps:
        1. Normalize text (characters + punctuation)
        2. Tokenize
        3. Split prefixes
        4. Remove stopwords
        5. Stem tokens
        6. Deduplicate tokens

        Args:
            text (str): input text
            return_structure (bool): if True, return dict with stages
        Returns:
            List of processed stems or dict of stages
        """
        normalized_text = self.normalizer.normalize(text)

        tokens = self.tokenizer.tokenize(normalized_text)

        tokens = split_tokens(tokens)

        filtered_tokens = self.stopwords.remove(tokens)

        stems = self.stemmer.stem(filtered_tokens)

        deduped_stems = list(dict.fromkeys(stems))

        if return_structure:
            return {
                "normalized_text": normalized_text,
                "tokens": tokens,
                "filtered_tokens": filtered_tokens,
                "stems": stems,
                "deduped_stems": deduped_stems
            }

        return deduped_stems