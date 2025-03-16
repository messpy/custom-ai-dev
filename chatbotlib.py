import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルを読み込む
load_dotenv()

def check_api_key():
    """APIキーが有効かどうかを確認する関数"""
    try:
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            return False, "APIキーが環境変数として設定されていません。"

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # テスト用の簡単なプロンプトを使用してチェック
        test_prompt = "APIキーの有効性を確認しています。"
        response = model.generate_content(test_prompt)
        if response and response.text:
            return True, "APIキーは有効です。"
        else:
            return False, "APIキーが無効です。"
    except Exception as e:
        return False, f"エラーが発生しました: {e}"

# APIキーの有効性をチェック
success, message = check_api_key()

# 結果を表示
print("APIキーのチェック結果:", success)
print("メッセージ:", message)
