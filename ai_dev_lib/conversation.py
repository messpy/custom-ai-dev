import json
from datetime import datetime

class Conversation:
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        """
        会話履歴にメッセージを追加する。
        role: "user" または "assistant"
        content: メッセージ内容
        """
        timestamp = datetime.now().isoformat()
        self.history.append({"role": role, "content": content, "timestamp": timestamp})

    def get_history(self):
        """会話履歴を返す"""
        return self.history

    def to_json(self):
        """会話履歴をJSON文字列に変換する"""
        return json.dumps(self.history, indent=2, ensure_ascii=False)

    def save_to_file(self, filename):
        """会話履歴を指定ファイルに保存する"""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.history, f, indent=2, ensure_ascii=False)

    def load_from_file(self, filename):
        """指定ファイルから会話履歴を読み込む"""
        with open(filename, "r", encoding="utf-8") as f:
            self.history = json.load(f)
