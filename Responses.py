from Data.Api import openai_api as API # API key
import openai

# fileopen = open("Data\Api.txt","r")
# API = fileopen.read()
# fileopen.close()
# API ="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"

# from dotenv import load_dotenv

openai.api_key = API
# load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log = None):
    filelog = open("Data/chat_log.txt","r")
    chat_log_template = filelog.read()
    filelog.close()


    if chat_log is None:
        chat_log = chat_log_template

    prompt = f"{chat_log}You: {question} \nManasvi: "
    response = completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0
    )
    answer = response.choices[0].text.strip()
    if answer not in chat_log:
        chat_log_template_update = chat_log_template +f"\nYou: {question}\nManasvi: {answer}"
        filelog = open("Data/chat_log.txt","w")
        filelog.write(chat_log_template_update)
        filelog.close()
    return answer

# print("let's talk")
# while True:
#     que = input("You: ")
#     print(f"Manasvi: {ReplyBrain(que)}")
