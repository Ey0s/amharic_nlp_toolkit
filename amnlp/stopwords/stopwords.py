import os

class StopwordRemover:

    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../resources/stopwords.txt"
        )

        with open(path, encoding="utf8") as f:
            # Normalize resource lines so trailing spaces or blank lines do not
            # prevent matches during token filtering.
            self.stopwords = {line.strip() for line in f if line.strip()}

    def remove(self, tokens):

        return [t for t in tokens if t not in self.stopwords]