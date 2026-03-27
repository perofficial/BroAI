"""
BroAI CLI demo — try presets interactively.
Usage:
    python -m demo.demo_cli
    humanizer-cli   (if installed via pip)
"""
import sys
from humanizer import humanize
from configs.presets import PRESETS

BANNER = """
╔═══════════════════════════════╗
║       BroAI  Humanizer        ║
║  Transform text. Sound human. ║
╚═══════════════════════════════╝
"""


def run_demo(text: str):
    print(f"\nOriginal:\n  {text}\n")
    for preset_name, params in PRESETS.items():
        result = humanize(text, **params)
        print(f"[{preset_name}]  {result}")
    print()


def main():
    print(BANNER)
    print("Available presets:", ", ".join(PRESETS.keys()))
    print("Press Ctrl+C to exit.\n")

    if len(sys.argv) > 1:
        run_demo(" ".join(sys.argv[1:]))
        return

    while True:
        try:
            text = input("Enter text: ").strip()
            if text:
                run_demo(text)
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
            break


if __name__ == "__main__":
    main()
