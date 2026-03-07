class POSTagger:

    def tag(self, tokens):

        results = []

        for t in tokens:

            if t.endswith("ች"):

                tag = "NOUN"

            elif t.endswith("አል"):

                tag = "VERB"

            else:

                tag = "UNK"

            results.append((t, tag))

        return results