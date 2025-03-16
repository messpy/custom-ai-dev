import os
from dotenv import load_dotenv
from google import genai

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数からAPIキーを取得
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY が設定されていません！")

# リクエストを送信してレスポンスを確認
try:
    # クライアントを作成
    client = genai.Client(api_key=api_key)
    
    # リクエストを送信
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Explain how AI works",
    )
    
    # レスポンスを出力
    print("レスポンス内容:")
    print(response.text)

except Exception as e:
    print(f"エラーが発生しました: {e}")
