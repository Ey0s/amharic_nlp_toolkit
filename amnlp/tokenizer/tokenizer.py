import regex as re
from amnlp.normalization.normalizer import AmharicNormalizer

TOKEN_PATTERN = re.compile(r"[\p{Script=Ethiopic}\d]+")

class AmharicTokenizer:

    def __init__(self):
        self.normalizer = AmharicNormalizer()

    def tokenize(self, text):
        # Remove punctuation before tokenizing so tokens like "ነው።" become "ነው"
        text = self.normalizer.normalize(text)
        return TOKEN_PATTERN.findall(text)