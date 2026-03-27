# BroAI – Human-like Text Generator for Synthetic Data

BroAI è una libreria Python progettata per generare **testo sintetico “human-like”** partendo da frasi o query di input. Permette di creare dataset realistici per training AI, test di chatbot, simulazioni utenti o data augmentation.

---

## ⚡ Features

* Trasforma testo in versioni più umane (“humanized”) con livelli di rumore e stili diversi
* Presets configurabili (`lite`, `balanced`, `aggressive`)
* Salvataggio automatico dei dataset generati in CSV (`output/synthetic_dataset.csv`)
* Facile integrazione con librerie per agenti AI come LangChain e LangGraph
* Open source: dizionari e presets modificabili

---

## 📂 Struttura della repo

```
BroAI/
├── configs/               # Presets configurabili
│   └── presets.py
├── data/                  # Input queries
│   └── clean_queries.txt
├── dictionaries/          # Dizionari slang, typo, grammar
├── humanizer/             # Core library
├── demo/                  # CLI demo
├── output/                # Salvataggi CSV
├── experiments/           # Test e tuning parametri
├── run.py                 # Script principale
├── requirements.txt
└── README.md
```

---

## 🚀 Installazione

```bash
git clone https://github.com/<tuo-username>/BroAI.git
cd BroAI
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

---

## ▶️ Uso

1. Inserisci le frasi di input in `data/clean_queries.txt`
2. Esegui lo script principale:

```bash
python run.py
```

3. Troverai il CSV generato in:

```bash
output/synthetic_dataset.csv
```

---

## ⚙️ Presets

Puoi modificare i parametri in `configs/presets.py`:

```python
PRESETS = {
    "lite": {"tone": "casual", "noise_level": 0.12},
    "balanced": {"tone": "casual", "noise_level": 0.2},
    "aggressive": {"tone": "genz", "noise_level": 0.25}
}
```

* `tone`: stile della frase
* `noise_level`: quantità di errori/variazioni introdotte

---

## 🧪 Testing & Valutazione

Puoi valutare il realismo delle frasi con `experiments/evaluate_output.py`.
Target score: **0.15–0.25** → realistico.

* Score troppo basso → testo troppo perfetto
* Score troppo alto → testo troppo rumoroso

---

## 📝 Contribuire

1. Forka il progetto
2. Aggiungi nuovi dizionari o presets
3. Apri una Pull Request

---

## 💡 Use Cases Aziendali

* Generazione di dataset per AI conversazionali
* Test e validazione di chatbot
* Data augmentation per NLP
* Simulazione utenti realistica

---

## 🔒 Note

* Output CSV e dati sensibili **non vanno tracciati su GitHub**
* Dizionari e presets sono open source e modificabili

---

## 🚀 Next Steps

Per una demo completa o landing freemium:

* Usa `demo/demo_cli.py` per provare preset in tempo reale
* Valuta output con `experiments/evaluate_output.py`
* Salva i dataset generati in `output/` per training o test

---

**BroAI** ti permette di trasformare frasi piatte in dataset **realistici, diversificati e pronti per l’uso aziendale o per ricerca NLP**.
