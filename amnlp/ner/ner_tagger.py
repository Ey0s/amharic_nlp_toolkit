class NERTagger:
    def __init__(self):
        self.locations = ["ኢትዮጵያ", "አዲስ", "አበባ", "አሜሪካ", "ኬንያ"]
        self.persons = ["አብይ", "መለስ", "ኃይለስላሴ"]
        self.organizations = ["UN", "AU", "WHO"]
        self.dates = ["ዛሬ", "ትላንት", "ነገ"]

    def recognize(self, tokens):
        entities = []

        for t in tokens:
            if t in self.locations:
                entities.append((t, "LOCATION"))

            elif t in self.persons:
                entities.append((t, "PERSON"))

            elif t in self.organizations:
                entities.append((t, "ORG"))

            elif t in self.dates:
                entities.append((t, "DATE"))

        return entities