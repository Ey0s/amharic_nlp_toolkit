import os

class StopwordRemover:

    def __init__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            "../resources/stopwords.txt"
        )

        with open(path, encoding="utf8") as f:

            self.stopwords = set(f.read().splitlines())

    def remove(self, tokens):

        return [t for t in tokens if t not in self.stopwords]