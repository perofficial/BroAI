import os
from humanizer import humanize

text = """Hi, I’ve been trying to access my account for the past couple of days but I keep getting an error message every time I try to log in. I already tried resetting my password but it still doesn’t work. Also, I’m not receiving any verification emails, so I’m kind of stuck. Can you please help me figure out what’s going on and how I can fix this as soon as possible?"""

# Generiamo il testo
humanized_text = humanize(text, tone="casual", noise_level=0.5)

# Percorso della cartella e nome del file .txt
output_dir = "/Users/matteoperoni/Documents/GitHub/email-spam-classifier/BroAI/output"
file_path = os.path.join(output_dir, "output_humanized.txt")

# Crea la cartella se non esiste
os.makedirs(output_dir, exist_ok=True)

# Salvataggio nel file di testo
with open(file_path, "w", encoding="utf-8") as f:
    f.write(humanized_text)

print(f"Testo salvato correttamente in: {file_path}")