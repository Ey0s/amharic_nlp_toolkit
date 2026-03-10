# Common Amharic prefixes
PREFIXES = ["በ", "ከ", "ለ", "ወደ", "የ", "በስተ", "በት"]

def split_prefix(word):
    """
    Split common Amharic prefixes from a word.
    Example: በትምህርት -> ['በ', 'ትምህርት']
    """

    for prefix in PREFIXES:
        if word.startswith(prefix) and len(word) > len(prefix):
            return [prefix, word[len(prefix):]]

    return [word]


def split_tokens(tokens):
    result = []

    for token in tokens:
        result.extend(split_prefix(token))

    return result