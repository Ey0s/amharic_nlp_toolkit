# amnlp

Lightweight Amharic NLP toolkit for normalization, tokenization, stopword filtering, stemming, and basic linguistic tagging.

## Table of Contents
- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core API](#core-api)
- [Data and Resource Pipelines](#data-and-resource-pipelines)
- [Testing](#testing)
- [Design Notes and Limitations](#design-notes-and-limitations)
- [Roadmap Ideas](#roadmap-ideas)

## Overview
`amnlp` provides rule-based building blocks for processing Amharic text.

Current capabilities:
- Ethiopic-script tokenization
- Orthographic normalization and punctuation cleanup
- Prefix splitting for common Amharic prefixes
- Stopword removal (file-backed list)
- Suffix-based stemming
- Basic morphology, POS, and NER heuristics
- Dictionary-backed word existence checks
- Composable mini pipeline abstraction

## System Architecture

### High-level processing flow

```text
Raw Text
   |
   v
AmharicNormalizer.normalize
   |
   v
AmharicTokenizer.tokenize
   |
   v
split_tokens (prefix splitter)
   |
   v
StopwordRemover.remove
   |
   v
AmharicStemmer.stem
   |
   v
Deduplicate (order-preserving)
   |
   v
Processed token list
```

### Component architecture

| Layer | Module | Class/Function | Responsibility |
|---|---|---|---|
| Public API | `amnlp/__init__.py` | `tokenize`, `stem`, `remove_stopwords` | Simple helper entry points |
| Pipeline | `amnlp/pipeline/processor.py` | `AmharicProcessor` | End-to-end text processing pipeline |
| Pipeline Infra | `amnlp/pipeline/pipeline.py` | `Pipeline` | Generic component chaining (`add`, `run`) |
| Tokenization | `amnlp/tokenizer/tokenizer.py` | `AmharicTokenizer` | Extract Ethiopic word tokens via regex |
| Sentence Split | `amnlp/tokenizer/sentence_tokenizer.py` | `SentenceTokenizer` | Split by sentence punctuation |
| Normalization | `amnlp/normalization/normalizer.py` | `AmharicNormalizer` | Character substitutions + punctuation removal |
| Stopwords | `amnlp/stopwords/stopwords.py` | `StopwordRemover` | Remove tokens from resource stopword list |
| Stemming | `amnlp/stemmer/stemmer.py` | `AmharicStemmer` | Rule-based suffix stripping |
| Morphology | `amnlp/morphology/analyzer.py` | `MorphAnalyzer` | Basic singular/plural heuristic |
| Morphology | `amnlp/morphology/prefix_splitter.py` | `split_prefix`, `split_tokens` | Split common prefixes |
| POS | `amnlp/pos/pos_tagger.py` | `POSTagger` | Rule-based POS tags |
| NER | `amnlp/ner/ner_tagger.py` | `NERTagger` | Gazetteer-style location lookup |
| Spellcheck | `amnlp/spellcheck/spell_checker.py` | `SpellChecker` | Dictionary membership check |
| Resources | `amnlp/resources/*` | text files | Stopwords and dictionary artifacts |

### Runtime dependencies
- `regex`: Unicode-aware regex used for Ethiopic tokenization/normalization.
- `datasets`: Used by dataset download script.
- `transformers`, `tokenizers`, `tqdm`: Present in dependency files for future/extended workflows.

## Project Structure

```text
amnlp/
├─ amnlp/
│  ├─ normalization/
│  ├─ tokenizer/
│  ├─ stopwords/
│  ├─ stemmer/
│  ├─ morphology/
│  ├─ pos/
│  ├─ ner/
│  ├─ spellcheck/
│  ├─ pipeline/
│  ├─ resources/
│  │  ├─ stopwords.txt
│  │  └─ amharic_dict.txt
│  ├─ __init__.py
│  └─ version.py
├─ scripts/
│  ├─ download_dataset.py
│  ├─ build_stopwords.py
│  └─ build_dictionary.py
├─ data/
│  └─ corpus.txt
├─ tests/
│  ├─ test_tokenizer.py
│  └─ test_pipeline.py
├─ examples/
│  └─ example.py
├─ requirements.txt
├─ pyproject.toml
└─ setup.py
```

## Installation

### 1. Clone and enter the project
```bash
git clone https://github.com/Ey0s/amharic_nlp_toolkit.git
cd amnlp
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install package in editable mode (recommended for development)
```bash
pip install -e .
```

## Quick Start

### End-to-end processor
```python
from amnlp.pipeline.processor import AmharicProcessor

text = "..."  # Amharic text
processor = AmharicProcessor()
result = processor.process(text)
print(result)
```

### Return intermediate pipeline stages
```python
from amnlp.pipeline.processor import AmharicProcessor

processor = AmharicProcessor()
stages = processor.process("...", return_structure=True)
print(stages["normalized_text"])
print(stages["tokens"])
print(stages["filtered_tokens"])
print(stages["stems"])
print(stages["deduped_stems"])
```

### Top-level helpers
```python
import amnlp

tokens = amnlp.tokenize("...")
stems = amnlp.stem(tokens)
clean = amnlp.remove_stopwords(tokens)
```

### Run included example
```bash
python examples/example.py
```

## Core API

### `AmharicProcessor` (`amnlp/pipeline/processor.py`)
- `process(text, return_structure=False)`:
  - Runs normalization -> tokenization -> prefix split -> stopword removal -> stemming -> deduplication.
  - Returns final list by default.
  - Returns stage dictionary if `return_structure=True`.

### `AmharicTokenizer` (`amnlp/tokenizer/tokenizer.py`)
- `tokenize(text)`:
  - Extracts Ethiopic-script tokens using `regex` pattern `\p{Script=Ethiopic}`.

### `SentenceTokenizer` (`amnlp/tokenizer/sentence_tokenizer.py`)
- `split(text)`:
  - Splits text into sentences by punctuation delimiters.

### `AmharicNormalizer` (`amnlp/normalization/normalizer.py`)
- `normalize(text)`:
  - Applies character normalization rules.
  - Removes punctuation characters matched by internal pattern.

### `StopwordRemover` (`amnlp/stopwords/stopwords.py`)
- `remove(tokens)`:
  - Drops tokens found in `amnlp/resources/stopwords.txt`.

### `AmharicStemmer` (`amnlp/stemmer/stemmer.py`)
- `stem(tokens)`:
  - Strips known suffixes from each token.

### `SpellChecker` (`amnlp/spellcheck/spell_checker.py`)
- `check(word)`:
  - Returns `True` if word is in `amnlp/resources/amharic_dict.txt`.

### `MorphAnalyzer` (`amnlp/morphology/analyzer.py`)
- `analyze(token)`:
  - Heuristic singular/plural label based on suffix.

### `POSTagger` (`amnlp/pos/pos_tagger.py`)
- `tag(tokens)`:
  - Rule-based tagging (`NOUN`, `VERB`, `UNK`).

### `NERTagger` (`amnlp/ner/ner_tagger.py`)
- `recognize(tokens)`:
  - Returns location entities from built-in list.

### Generic `Pipeline` (`amnlp/pipeline/pipeline.py`)
- `add(component)` then `run(text)`:
  - Component functions are called in insertion order.

## Data and Resource Pipelines

### 1. Download corpus
```bash
python scripts/download_dataset.py
```
Downloads and writes corpus lines to `data/corpus.txt`.
Note: `data/corpus.txt` is treated as a local large artifact and is git-ignored.

### 2. Build stopwords from corpus frequency
```bash
python scripts/build_stopwords.py
```
Creates top-frequency stopwords list in `amnlp/resources/stopwords.txt`.

### 3. Build dictionary from corpus vocabulary
```bash
python scripts/build_dictionary.py
```
Creates sorted vocabulary dictionary in `amnlp/resources/amharic_dict.txt`.

### Current artifact sizes in this repository snapshot
- `data/corpus.txt`: 5,796,660 lines (generated locally, not tracked in git)
- `amnlp/resources/stopwords.txt`: 165 lines
- `amnlp/resources/amharic_dict.txt`: 2,641,544 lines

## Testing

Run tests:
```bash
pytest -q
```

Current tests in repository:
- `tests/test_tokenizer.py` (tokenization presence assertion)
- `tests/test_pipeline.py` (present but currently empty)

## Design Notes and Limitations
- Most components are rule-based and intentionally lightweight.
- POS, NER, and morphology are heuristic baselines, not model-based taggers.
- Stemming and normalization coverage is limited to defined rules.
- Very large dictionary file can increase startup memory for spellcheck.
- Resource generation scripts assume `data/corpus.txt` exists and use relative paths from repo root.

## Roadmap Ideas
- Expand normalization/stemming rules with linguistic evaluation.
- Replace heuristic POS/NER with trainable or transformer-backed models.
- Add benchmark datasets and quality metrics (precision/recall/F1).
- Improve test coverage across all modules.
- Add CLI entry points for common tasks.
