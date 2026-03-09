class AmharicStemmer:
    noun_suffixes = ["ዎች", "ች", "ን", "ህ", "ሽ", "ዋ"]

    def stem(self, tokens, return_mapping=False):
        stems = []
        mapping = {}

        for token in tokens:
            original = token
            changed = True
            while changed and len(token) > 3:
                changed = False
                for s in self.noun_suffixes:
                    if token.endswith(s):
                        token = token[:-len(s)]
                        changed = True
                        break
            stems.append(token)
            mapping[original] = token

        return mapping if return_mapping else stems