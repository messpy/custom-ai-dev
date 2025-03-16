import json

def read_json(filename):
    """指定ファイルから JSON データを読み込み、オブジェクトとして返す"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json(data, filename):
    """オブジェクトを JSON として指定ファイルに書き出す"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
