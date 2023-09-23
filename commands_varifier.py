from Data.Api import openai_api as API # API key
import openai
import json

# fileopen = open("Data\Api.txt","r")
# API = fileopen.read()
# fileopen.close()
# from dotenv import load_dotenv

openai.api_key = API
# load_dotenv()
completion = openai.Completion()



def varify(question,apps_list,command_log = None):
    filelog = open("Data/command_varify.txt","r")
    chat_log_template = filelog.read()
    filelog.close()

    if command_log is None:
        command_log = chat_log_template

    # prompt = f"{command_log}You: {question} \n: "
    prompt=f"{command_log}Q: {question} \n",
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
    # print(answer)

    if answer not in command_log:
        chat_log_template_update = chat_log_template + f"\n\nQ: {question}\n{answer}"
        filelog = open("Data/command_varify.txt","w")
        filelog.write(chat_log_template_update)
        filelog.close()

    if json.loads(answer)['Category'] == 'open app':
        
        app = json.loads(answer)["app name"]
        if app not in apps_list:

            answer = '{"Category": "app not found","speak": "there is no app with name '+app+'"}'
            
    return json.loads(answer)

# print("let's talk")
# while True:
#     que = input("You: ")
#     print(f"{varify(que,'00',['instagram'])}")
