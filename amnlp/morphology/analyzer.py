class MorphAnalyzer:

    def analyze(self, token):

        result = {}

        if token.endswith("ች"):

            result["number"] = "plural"

        else:

            result["number"] = "singular"

        return result