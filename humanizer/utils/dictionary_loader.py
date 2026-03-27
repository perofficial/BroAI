import json

def load_dictionary(path):
    print("\n🔍 Loading file:", path)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

        print("📄 Content preview:", repr(content[:50]))

        return json.loads(content)