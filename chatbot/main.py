import openai

openai.api_key = "API_KEY"

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
                {"role": "chat", "content": "Hello!"}  
            ]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I encountered an error."

if __name__ == "__main__":
    print("Welcome! Start chatting with the bot (type 'quit', 'exit', or 'bye' to end the conversation).\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)