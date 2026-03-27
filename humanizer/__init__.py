# humanizer/__init__.py

# Import principale per la funzione humanize
from .core import humanize

# Import della pipeline principale
from .pipeline import HumanizerPipeline

# Opzionale: puoi anche esporre utility o classi aggiuntive se servono
# from .noise import inject_noise
# from .style import apply_style
# from .utils.dictionary_loader import load_dictionary

__all__ = [
    "humanize",
    "HumanizerPipeline",
    # "inject_noise",
    # "apply_style",
    # "load_dictionary"
]