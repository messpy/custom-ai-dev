from conversation import Conversation
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
