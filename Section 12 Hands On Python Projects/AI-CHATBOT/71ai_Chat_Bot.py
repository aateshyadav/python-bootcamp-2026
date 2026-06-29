import os
from openai import OpenAI

#key="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"

messages = []

client = OpenAI(
    api_key=key,  # This is the default and can be omitted
)

def completion(message):
    global messages

    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o"
    )

    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }

    messages.append(message)

    print(f"Jarvis: {message['content']}")

if __name__ == "__main__":
    print("Jarvis: Hi I am Jarvis, How may I help you\n")

    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)
        