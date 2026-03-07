class AmharicStemmer:

    suffixes = [
        "ዎች",
        "ች",
        "ን",
        "ህ",
        "ሽ",
        "ዋ"
    ]

    def stem(self, tokens):

        stems = []

        for token in tokens:

            for s in self.suffixes:

                if token.endswith(s):

                    token = token[:-len(s)]

            stems.append(token)

        return stems