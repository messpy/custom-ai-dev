import os
from dotenv import load_dotenv
from utils.checker import check_api_response

# .envファイルを読み込む
load_dotenv()

if __name__ == "__main__":
    print("環境チェックおよびAPIレスポンスの確認を開始します...")

    # 環境変数の確認
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("環境変数 GEMINI_API_KEY が設定されていません！")
        exit(1)

    print("環境変数 GEMINI_API_KEY が設定されています。")

    # APIレスポンスの確認
    try:
        response = check_api_response(api_key)
        print("APIレスポンス:", response)
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        exit(1)

    print("すべてのチェックが完了しました。メイン処理を開始します...")
