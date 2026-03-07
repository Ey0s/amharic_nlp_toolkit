import regex as re

words = set()

pattern = re.compile(r'[\u1200-\u137F]+')

with open("./data/corpus.txt", encoding="utf8") as f:

    for line in f:

        tokens = pattern.findall(line)

        words.update(tokens)

with open("./amnlp/resources/amharic_dict.txt", "w", encoding="utf8") as f:

    for w in sorted(words):

        f.write(w + "\n")