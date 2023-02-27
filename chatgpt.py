# from ChatGPT.src.revChatGPT.V1 import Chatbot
from revChatGPT.V1 import Chatbot
from config import session_token, email, password

def start_chatgpt():
    prev_text = ""
    chatbot = Chatbot(config={
    #   "email": email,
    #   "password": password,
    "session_token": session_token,
    # "proxy":
    })
    for data in chatbot.ask("你好",):
        # pdb.set_trace()
        message = data["message"][len(prev_text) :]
        conversation_id = data["conversation_id"]
        parent_id = data["parent_id"]
        # print(message, end="", flush=True)
        prev_text = data["message"]
    return chatbot, conversation_id, parent_id, prev_text

def chatgpt(text, chatbot, conversation_id=None, parent_id=None):
    prev_text = ""
    for data in chatbot.ask(
        text, conversation_id = conversation_id, parent_id = parent_id,
    ):
    # pdb.set_trace()
        message = data["message"][len(prev_text) :]
        conversation_id = data["conversation_id"]
        parent_id = data["parent_id"]
        # print(message, end="", flush=True)
        prev_text = data["message"]
        # print(prev_text)
    return prev_text