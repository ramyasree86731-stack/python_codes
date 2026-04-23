from openai import OpenAI

client = OpenAI(api_key="")

def start_chatbot():
    message = [{"role":"system","content":"you are a helper and assistant"}]

    print("Idealabs chatbot,Type 'quit' to exit")

    while True:
        user_input=input("you: ")
        if user_input.lower() in ["quit","exit"]:
            break
        message.append({"role":"user","content":user_input})
        response = client.chat.completions.create(
            model="gpt-40-mini",
            messages=messages,
            temperature=0.7,
            )
        assistant_reply=response,choices[0].message.content
        print("Idealabs:{assistant_reply}")

        message.append({"role":"assistant","content":assistant_reply})

if __name__== "__main__":
    start_chatbot()
