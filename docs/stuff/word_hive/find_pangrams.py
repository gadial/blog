import json
with open("dictionary.json", "r", encoding="utf8") as f:
    words = json.load(f)
pangrams = [word for word in words if len(set(word)) == 7]
with open("pangrams.json", "w", encoding="utf8") as f:
    json.dump(pangrams, f, ensure_ascii=False)