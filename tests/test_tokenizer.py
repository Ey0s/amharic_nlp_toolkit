from amnlp.tokenizer.tokenizer import AmharicTokenizer

def test_tokenizer():

    tok = AmharicTokenizer()

    tokens = tok.tokenize("ኢትዮጵያ ታላቅ ሀገር")

    assert "ኢትዮጵያ" in tokens