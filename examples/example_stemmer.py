from amnlp.stemmer.stemmer import AmharicStemmer
tokens = ['ተማሪዎች', 'ትምህርት', 'እየተማሩ']
stemmer = AmharicStemmer()

# Just stems
print(stemmer.stem(tokens))
# ['ተማሪ', 'ትምህርት', 'እየተማሩ']

# Original -> stemmed mapping
print(stemmer.stem(tokens, return_mapping=True))
# {'ተማሪዎች': 'ተማሪ', 'ትምህርት': 'ትምህርት', 'እየተማሩ': 'እየተማሩ'}