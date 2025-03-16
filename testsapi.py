import os
import zipfile

# プロジェクトのルートディレクトリ名
project_root = "ai_dev_lib"

# 各ファイルの定義
files = {
    os.path.join(project_root, "__init__.py"): "",
    os.path.join(project_root, "conversation.py"):
r'''import json
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
''',
    os.path.join(project_root, "llm_provider.py"):
r'''import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class LLMProvider:
    def __init__(self, provider="gemini", model_name="gemini-1.5-flash"):
        """
        LLMProvider クラス
        provider: "gemini"（現時点では Gemini のみサポート）
        model_name: 利用するモデル名（例: gemini-1.5-flash）
        """
        self.provider = provider
        self.model_name = model_name
        self.chat = None
        if provider == "gemini":
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("Gemini APIキーが環境変数に設定されていません。")
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name)
            # 会話用のチャットを開始
            self.chat = model.start_chat(history=[])
        else:
            raise NotImplementedError("指定されたプロバイダーはサポートされていません。")

    def send_message(self, message):
        """
        ユーザーのメッセージを送信し、LLMの応答テキストを返す
        """
        if self.chat is None:
            raise ValueError("チャットが初期化されていません。")
        response = self.chat.send_message(message)
        return response.text
''',
    os.path.join(project_root, "json_utils.py"):
r'''import json

def read_json(filename):
    """指定ファイルから JSON データを読み込み、オブジェクトとして返す"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json(data, filename):
    """オブジェクトを JSON として指定ファイルに書き出す"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
''',
    os.path.join(project_root, "main.py"):
r'''from conversation import Conversation
from llm_provider import LLMProvider

def main():
    conv = Conversation()
    llm = LLMProvider()  # Gemini を利用する場合。必要に応じてモデル名を指定可能

    print("チャットボットです。何か質問はありますか？（終了するには「終了」と入力してください）")
    while True:
        user_input = input("質問: ")
        if user_input.strip() == "終了":
            print("チャット終了")
            break
        conv.add_message("user", user_input)
        response = llm.send_message(user_input)
        print("応答:", response)
        conv.add_message("assistant", response)

    # 会話履歴をJSONファイルに保存
    conv.save_to_file("conversation_history.json")
    print("会話履歴を conversation_history.json に保存しました。")

if __name__ == "__main__":
    main()
'''
}

# ファイル生成
for filepath, content in files.items():
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# ZIPファイル作成
zip_filename = "ai_dev_lib.zip"
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for foldername, subfolders, filenames in os.walk(project_root):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            arcname = os.path.relpath(file_path, os.path.dirname(project_root))
            zipf.write(file_path, arcname)

print(f"ZIPファイル {zip_filename} が生成されました。")
