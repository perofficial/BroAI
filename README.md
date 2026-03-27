# BroAI – Human-like Text Generator for Synthetic Data

BroAI is a Python library designed to generate **realistic human-like text** from clean input sentences. It creates synthetic datasets for AI training, chatbot testing, user simulation, and NLP data augmentation.

---

## Features

- Transforms text into more human versions with configurable noise levels and styles
- Configurable presets: `lite`, `balanced`, `aggressive`
- FastAPI web server ready for production deployment
- CLI demo for quick interactive testing
- Automatic CSV dataset export
- Easy integration with LangChain, LangGraph, and other AI agent frameworks
- Open source: all dictionaries and presets are editable

---

## Repository Structure

```
BroAI/
├── humanizer/               # Core library
│   ├── __init__.py
│   ├── core.py              # Public API: humanize()
│   ├── pipeline.py          # HumanizerPipeline orchestrator
│   ├── style.py             # Tone transformation (casual, formal, genz)
│   ├── noise.py             # Noise injection (typos, fillers, drops)
│   └── utils/
│       ├── dictionary_loader.py
│       └── random_utils.py
├── configs/                 # Presets and YAML configs
│   ├── presets.py
│   ├── presets.yaml
│   ├── default.yaml
│   ├── noise_profiles.yaml
│   └── personas.yaml
├── config/
│   └── production.yaml      # Production server config
├── dictionaries/            # Word replacement dictionaries
│   ├── typos/
│   │   ├── english.json
│   │   └── italian.json
│   ├── slang/
│   │   ├── genz.json
│   │   └── italian_genz.json
│   └── grammar/
│       └── contractions.json
├── data/
│   └── clean_queries.txt    # Input sentences
├── output/                  # Generated datasets (git-ignored)
├── experiments/             # Evaluation and tuning scripts
│   ├── evaluate_output.py
│   ├── evaluator.py
│   └── tune_params.py
├── demo/
│   └── demo_cli.py          # Interactive CLI
├── test/
│   └── test_basic.py        # Unit tests
├── web_api.py               # FastAPI production server
├── run.py                   # Batch dataset generation script
├── pyproject.toml
├── requirements.txt
└── requirements-dev.txt
```

---

## Installation

```bash
git clone https://github.com/your-username/BroAI.git
cd BroAI
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

For development (includes pytest):

```bash
pip install -r requirements-dev.txt
```

---

## Quick Start

### Python API

```python
from humanizer import humanize

# Basic usage
result = humanize("How can I reset my password?", tone="casual", noise_level=0.2)
print(result)
# → "how can i reset my password?"

# Gen Z style with high noise
result = humanize("This is really good", tone="genz", noise_level=0.35)
print(result)
# → "this is literally fire bro"

# Formal (expand contractions, clean grammar)
result = humanize("I can't access my account", tone="formal", noise_level=0.05)
print(result)
# → "I cannot access my account"
```

### Batch Dataset Generation

```bash
python run.py
```

Reads from `data/clean_queries.txt`, generates 3 variations per query (lite / balanced / aggressive), saves to `output/synthetic_dataset.csv`.

### CLI Demo

```bash
python -m demo.demo_cli
# or, if installed via pip:
humanizer-cli
```

### FastAPI Server

```bash
uvicorn web_api:app --reload
```

Then POST to `http://localhost:8000/humanize`:

```json
{
  "text": "I cannot access my account",
  "tone": "casual",
  "noise_level": 0.2
}
```

Response:

```json
{
  "original": "I cannot access my account",
  "humanized": "i can't access my account",
  "tone": "casual",
  "noise_level": 0.2
}
```

Health check: `GET http://localhost:8000/health`

---

## Presets

| Preset     | Tone   | Noise | Description                              |
|------------|--------|-------|------------------------------------------|
| lite       | casual | 0.10  | Light touch — contractions only          |
| balanced   | casual | 0.20  | Natural human tone, mild imperfections   |
| aggressive | genz   | 0.35  | Heavy slang, typos, dropped words        |

Customize in `configs/presets.py` or `configs/presets.yaml`:

```python
PRESETS = {
    "lite":       {"tone": "casual", "noise_level": 0.10},
    "balanced":   {"tone": "casual", "noise_level": 0.20},
    "aggressive": {"tone": "genz",   "noise_level": 0.35},
}
```

Parameters:

- `tone`: `casual` | `formal` | `genz`
- `noise_level`: `0.0` (clean) → `1.0` (very noisy)

---

## Noise Profiles

Defined in `configs/noise_profiles.yaml`. Controls the mix of typos, fillers, and word drops:

```yaml
medium_noise:
  level: 0.15
  typo_weight: 0.5
  filler_weight: 0.3
  drop_weight: 0.2
```

---

## Personas

Defined in `configs/personas.yaml`. Pre-built user archetypes:

| Persona        | Tone   | Noise | Behavior              |
|----------------|--------|-------|-----------------------|
| impatient_user | casual | 0.30  | Short sentences, drops|
| confused_user  | casual | 0.40  | Repetition, fillers   |
| genz_user      | genz   | 0.20  | Slang boost           |
| formal_user    | formal | 0.05  | Strict grammar        |

---

## Evaluation

Run the evaluator on generated output:

```bash
python -m experiments.evaluate_output
```

Target score: **0.15 – 0.25** → realistic.

- Score too low → text is too clean, increase `noise_level`
- Score too high → text is too noisy, decrease `noise_level`

### Parameter Tuning

```bash
python -m experiments.tune_params
```

Grid-searches across all tone × noise_level combinations and highlights which hit the realistic range.

---

## Running Tests

```bash
pytest test/
```

---

## Extending BroAI

### Add a new dictionary

Drop a `.json` file into the appropriate folder under `dictionaries/`:

```json
{
  "hello": ["hey", "sup"],
  "goodbye": ["later", "cya"]
}
```

Then load it in `style.py` or `noise.py` using `load_dictionary()`.

### Add a new tone

In `humanizer/style.py`, add a branch in `apply_style()`:

```python
elif tone == "my_tone":
    return _my_tone(text)
```

### Add a new preset

In `configs/presets.py`:

```python
"my_preset": {"tone": "my_tone", "noise_level": 0.25}
```

---

## Use Cases

- Generating datasets for conversational AI training
- Chatbot testing and validation
- NLP data augmentation
- Realistic user simulation
- Synthetic dataset generation for classifiers

---

## Notes

- Output CSVs and sensitive data are git-ignored by default
- All dictionaries and presets are open source and editable
- The `output/` folder is created automatically on first run

---

## License

MIT License — Copyright (c) 2026 Matteo Peroni
