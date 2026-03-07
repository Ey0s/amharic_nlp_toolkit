class NERTagger:

    locations = ["ኢትዮጵያ", "አዲስ", "አበባ"]

    def recognize(self, tokens):

        entities = []

        for t in tokens:

            if t in self.locations:

                entities.append((t, "LOCATION"))

        return entities