from amnlp.tokenizer.tokenizer import AmharicTokenizer
from amnlp.normalization.normalizer import AmharicNormalizer
from amnlp.stopwords.stopwords import StopwordRemover
from amnlp.stemmer.stemmer import AmharicStemmer

# Only noun/adjective prefixes
PREFIXES = ["በ", "ከ", "ለ", "ወደ", "የ", "በስተ", "በት"]

def split_prefix(word):
    """
    Split noun/adjective prefixes.
    Do NOT split verb conjugation prefixes (እ, ይ, ተ)
    """
    for prefix in PREFIXES:
        if word.startswith(prefix) and len(word) > len(prefix) + 2:
            return [word[len(prefix):]]
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
        Full NLP pipeline:
        1. Normalize
        2. Tokenize
        3. Split noun/adjective prefixes
        4. Remove stopwords
        5. Stem nouns/adjectives
        6. Deduplicate
        """
        normalized_text = self.normalizer.normalize(text)
        tokens = self.tokenizer.tokenize(normalized_text)
        tokens = split_tokens(tokens)
        filtered_tokens = self.stopwords.remove(tokens)

        # Stem nouns/adjectives only
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