from datasets import load_dataset

ds = load_dataset("rasyosef/amharic-sentences-corpus")

sentences = ds["train"]["text"]

with open("./data/corpus.txt", "w", encoding="utf8") as f:

    for s in sentences:

        f.write(s + "\n")