"""
Tests for the 4 bug fixes:
1. Normalizer no longer strips punctuation in normalize() — only in normalize_and_strip()
2. Processor uses prefix_splitter.split_tokens (no duplication)
3. version.py and setup.py share the same version string
4. amnlp.__init__ exposes a top-level normalize()
"""

import amnlp
from amnlp.normalization.normalizer import AmharicNormalizer
from amnlp.tokenizer.tokenizer import AmharicTokenizer
from amnlp.tokenizer.sentence_tokenizer import SentenceTokenizer
from amnlp.morphology.prefix_splitter import split_tokens
from amnlp.pipeline.processor import AmharicProcessor
from amnlp.version import __version__
import re
import os


# ── Fix 1: normalize() preserves sentence boundaries ──────────────────────────

def test_normalize_preserves_sentence_punctuation():
    normalizer = AmharicNormalizer()
    text = "ኢትዮጵያ ታላቅ ሀገር ናት። አዲስ አበባ ዋና ከተማ ናት።"
    result = normalizer.normalize(text)
    # Sentence boundary '።' must survive plain normalize()
    assert "።" in result

def test_normalize_and_strip_removes_punctuation():
    normalizer = AmharicNormalizer()
    text = "ኢትዮጵያ ታላቅ ሀገር ናት። አዲስ አበባ ዋና ከተማ ናት።"
    result = normalizer.normalize_and_strip(text)
    assert "።" not in result

def test_sentence_tokenizer_sees_boundaries():
    """SentenceTokenizer must work correctly because normalize() doesn't eat '።'"""
    st = SentenceTokenizer()
    text = "ኢትዮጵያ ታላቅ ሀገር ናት። አዲስ አበባ ዋና ከተማ ናት።"
    normalizer = AmharicNormalizer()
    sentences = st.split(normalizer.normalize(text))
    assert len(sentences) == 2

def test_word_tokenizer_still_strips_punctuation():
    """AmharicTokenizer must still return clean tokens without punctuation."""
    tok = AmharicTokenizer()
    tokens = tok.tokenize("ኢትዮጵያ ታላቅ ሀገር ናት།")
    assert all("།" not in t and "።" not in t for t in tokens)
    assert "ኢትዮጵያ" in tokens


# ── Fix 2: processor uses prefix_splitter, no duplicate logic ─────────────────

def test_processor_imports_split_tokens_from_prefix_splitter():
    """processor.py must NOT define its own split_tokens; it imports from prefix_splitter."""
    import amnlp.pipeline.processor as proc_module
    import amnlp.morphology.prefix_splitter as ps_module
    # The split_tokens name in processor must be the same object as in prefix_splitter
    assert proc_module.split_tokens is ps_module.split_tokens

def test_prefix_splitter_consistent_with_processor():
    """split_tokens from prefix_splitter must produce same result when called via processor."""
    tokens = ["በትምህርት", "ለሰው", "ኢትዮጵያ"]
    from amnlp.morphology.prefix_splitter import split_tokens as ps_split
    direct = ps_split(tokens)
    # Run it through processor internals by comparing pipeline tokens
    processor = AmharicProcessor()
    result = processor.process("በትምህርት ለሰው ኢትዮጵያ", return_structure=True)
    assert result["tokens"] == direct


# ── Fix 3: single version source of truth ─────────────────────────────────────

def test_version_files_are_in_sync():
    """setup.py must read its version from version.py — both must match."""
    setup_path = os.path.join(os.path.dirname(__file__), "..", "setup.py")
    with open(setup_path, encoding="utf-8") as f:
        setup_src = f.read()
    # setup.py should NOT have a hardcoded version string like version="0.1.x"
    assert 'version="0.1' not in setup_src, (
        "setup.py has a hardcoded version — it should read from version.py"
    )
    # setup.py should reference read_version or version.py
    assert "version.py" in setup_src or "read_version" in setup_src

def test_version_value_is_consistent():
    """The version read at import time must match what's in version.py."""
    assert amnlp.__version__ == __version__ if hasattr(amnlp, "__version__") else True
    # Direct check: version.py value is the real canonical one
    assert __version__ == "0.1.1"


# ── Fix 4: top-level normalize() is exposed ───────────────────────────────────

def test_normalize_is_in_public_api():
    assert hasattr(amnlp, "normalize"), "amnlp.normalize must be exposed in __init__.py"
    assert callable(amnlp.normalize)

def test_top_level_normalize_does_character_substitution():
    text = "ሐበሻ"  # ሐ should normalize to ሀ
    result = amnlp.normalize(text)
    assert result == "ሀበሻ"

def test_top_level_normalize_preserves_punctuation():
    text = "ሐበሻ ናት። ጥሩ ሀገር።"
    result = amnlp.normalize(text)
    assert "።" in result  # punctuation must NOT be stripped
