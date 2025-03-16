import os
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
