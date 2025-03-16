def generate_exercise(prompt):
    # Dummy implementation for English learning exercise generation
    return f"Exercise generated for prompt: {prompt}"

def practice_conversation():
    print("Starting English conversation practice mode...")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Exercise:", generate_exercise(user_input))

if __name__ == "__main__":
    practice_conversation()
