import csv
import json

def test_csv_column_count():
    with open('profiles1.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        assert len(headers) == 12

def test_csv_row_count():
    with open('profiles1.csv', 'r', encoding='utf-8') as f:
        rows = list(csv.reader(f))
        assert len(rows) - 1 >= 900  # minus header

def test_json_keys():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    expected_keys = {
        'id', 'first_name', 'last_name', 'email', 'gender',
        'ip_address', 'city', 'country', 'company', 'title',
        'phone', 'birthdate'
    }
    assert set(data[0].keys()) == expected_keys

def test_json_row_count():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert len(data) >= 900
