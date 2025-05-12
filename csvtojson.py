import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    csv_to_json("profiles1.csv", "data.json")
