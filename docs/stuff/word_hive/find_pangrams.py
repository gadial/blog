import json
def lower(word):
    lower_map = {
        'ך': 'כ',
        'ם': 'מ',
        'ן': 'נ',
        'ף': 'פ',
        'ץ': 'צ',
    }
    return "".join([lower_map.get(c, c) for c in word])

with open("dictionary.json", "r", encoding="utf8") as f:
    words = json.load(f)
pangrams = [lower(word) for word in words if len(set(lower(word))) == 7]
with open("pangrams.json", "w", encoding="utf8") as f:
    json.dump(pangrams, f, ensure_ascii=False)