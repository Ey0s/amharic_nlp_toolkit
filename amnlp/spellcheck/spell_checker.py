import os

class SpellChecker:

    def __init__(self):
        """Load the Amharic dictionary from the resources folder and use it """
        path = os.path.join(
            os.path.dirname(__file__),
            "../resources/amharic_dict.txt"
        )

        with open(path, encoding="utf8") as f:

            self.words = set(f.read().splitlines())

    def check(self, word):

        return word in self.words