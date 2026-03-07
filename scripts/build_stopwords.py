from collections import Counter
import regex as re

counter = Counter()

pattern = re.compile(r'[\u1200-\u137F]+')

with open("./data/corpus.txt", encoding="utf8") as f:

    for line in f:

        tokens = pattern.findall(line)

        counter.update(tokens)

common = [w for w, _ in counter.most_common(200)]

with open("./amnlp/resources/stopwords.txt", "w", encoding="utf8") as f:

    for w in common:

        f.write(w + "\n")