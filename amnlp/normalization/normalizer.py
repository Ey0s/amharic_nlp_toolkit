import regex as re


class AmharicNormalizer:

    NORMALIZATION_RULES = {
        "ሀ": "ሐ",
        "ሰ": "ሠ",
        "ጸ": "ፀ",
        "ኀ": "ሐ",
        "አ": "ኣ"
    }

    PUNCTUATION_PATTERN = re.compile(r"[።፣፤፥!?.,]")

    def normalize(self, text):

        for src, target in self.NORMALIZATION_RULES.items():
            text = text.replace(src, target)

        text = self.PUNCTUATION_PATTERN.sub("", text)

        return text