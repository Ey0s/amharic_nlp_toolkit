import regex as re


class AmharicNormalizer:

    NORMALIZATION_RULES = {
        # Normalize ሀ
        "ሐ": "ሀ", "ኀ": "ሀ", "ኃ": "ሀ", "ሓ": "ሀ", "ኻ": "ሀ",
        "ሑ": "ሁ", "ኁ": "ሁ", "ዅ": "ሁ",
        "ሒ": "ሂ", "ኂ": "ሂ", "ዂ": "ሂ",
        "ሔ": "ሄ", "ኄ": "ሄ", "ዄ": "ሄ",
        "ሕ": "ህ", "ኅ": "ህ",
        "ሖ": "ሆ", "ኆ": "ሆ",
        # Normalize ሰ
        "ሠ": "ሰ", "ሡ": "ሱ", "ሢ": "ሲ", "ሣ": "ሳ", "ሤ": "ሴ", "ሥ": "ስ", "ሦ": "ሶ",
        # Normalize ጸ
        "ፀ": "ጸ", "ፁ": "ጹ", "ፂ": "ጺ", "ፃ": "ጻ", "ፄ": "ጼ", "ፅ": "ጽ", "ፆ": "ጾ",
        # Normalize አ
        "ዐ": "አ", "ዑ": "ኡ", "ዒ": "ኢ", "ዓ": "አ", "ኣ": "አ", "ዔ": "ኤ", "ዕ": "እ", "ዖ": "ኦ"
    }

    PUNCTUATION_PATTERN = re.compile(r"[።፣፤፥!?.,]")

    def normalize(self, text):

        for src, target in self.NORMALIZATION_RULES.items():
            text = text.replace(src, target)

        text = self.PUNCTUATION_PATTERN.sub("", text)

        return text
