import json


def save_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
