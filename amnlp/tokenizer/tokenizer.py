import regex as re
from amnlp.normalization.normalizer import AmharicNormalizer

TOKEN_PATTERN = re.compile(r"[\p{Script=Ethiopic}\d]+")

class AmharicTokenizer:

    def __init__(self):
        self.normalizer = AmharicNormalizer()

    def tokenize(self, text):
        # Use normalize_and_strip so punctuation is removed before word extraction
        # but sentence boundaries in the original text are not affected.
        text = self.normalizer.normalize_and_strip(text)
        return TOKEN_PATTERN.findall(text)