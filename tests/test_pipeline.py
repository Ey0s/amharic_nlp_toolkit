from amnlp.pipeline.processor import AmharicProcessor
from amnlp.stemmer.stemmer import AmharicStemmer


def test_stemmer_trims_common_verb_suffix():
	assert AmharicStemmer().stem(["ይማራሉ"]) == ["ይማራ"]


def test_pipeline_returns_intermediate_stages():
	result = AmharicProcessor().process("ተማሪዎች በትምህርት ቤት ይማራሉ", return_structure=True)

	# prefix_splitter splits "በትምህርት" into ["በ", "ትምህርት"]
	assert result["tokens"] == ["ተማሪዎች", "በ", "ትምህርት", "ቤት", "ይማራሉ"]
	# "በ" is a stopword so it's filtered before stemming
	assert result["filtered_tokens"] == ["ተማሪዎች", "ትምህርት", "ቤት", "ይማራሉ"]
	assert result["stems"] == ["ተማሪ", "ትምህርት", "ቤት", "ይማራ"]
