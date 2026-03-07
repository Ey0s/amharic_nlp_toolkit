import regex as re

TOKEN_PATTERN = re.compile(r"[\p{Script=Ethiopic}]+")

class AmharicTokenizer:

    def tokenize(self, text):

        return TOKEN_PATTERN.findall(text)