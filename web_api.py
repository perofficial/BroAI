# web_api.py
# FastAPI server per collegare BroAI Humanizer al web

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yaml
import os
from humanizer import HumanizerPipeline

# --- 1️⃣ Caricamento configurazione production.yaml ---
CONFIG_DIR = os.path.join(os.path.dirname(__file__), 'config')
PROD_CONFIG_PATH = os.path.join(CONFIG_DIR, 'production.yaml')

if not os.path.exists(PROD_CONFIG_PATH):
    raise RuntimeError(f'File di configurazione {PROD_CONFIG_PATH} non trovato.')

with open(PROD_CONFIG_PATH, 'r') as f:
    config = yaml.safe_load(f)

# Controllo se il config è valido
if config is None:
    raise RuntimeError(f'File di configurazione {PROD_CONFIG_PATH} è vuoto o malformato')

print("✅ Config caricata correttamente:")
for section, values in config.items():
    print(f" - {section}: {values}")

# --- 2️⃣ Inizializzazione pipeline Humanizer ---
pipeline = HumanizerPipeline(
    tone=config.get('pipeline', {}).get('tone', 'dynamic'),
    noise_level=config.get('pipeline', {}).get('noise_level', 'adaptive'),
    typo_distribution=config.get('noise', {}).get('typo_distribution', {}),
    contextual_noise=config.get('noise', {}).get('contextual_noise', False),
    adaptive_noise=config.get('noise', {}).get('adaptive_noise', False),
    persona_adaptation=config.get('style', {}).get('persona_adaptation', False),
    memory_based_variation=config.get('style', {}).get('memory_based_variation', False)
)

# --- 3️⃣ Creazione FastAPI app ---
app = FastAPI(title="BroAI Humanizer API")

# Input schema
class InputText(BaseModel):
    text: str

# --- 4️⃣ Endpoint principale ---
@app.post("/humanize")
def humanize_text(input: InputText):
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Input vuoto")

    humanized = pipeline.humanize([input.text])
    return {"humanized_text": humanized[0]}

# --- 5️⃣ Endpoint di test rapido ---
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "pipeline_tone": config.get('pipeline', {}).get('tone', 'dynamic')
    }