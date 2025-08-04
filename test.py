import requests
import json
from openai import OpenAI


class My_Rag:

    def __init__(self):
        # 你的服务地址
        self.url = "http://127.0.0.1:8002/ask"

    def ask_q(self,ask, qty=1):
        response = requests.post(self.url, json={"question": ask, "top_k": qty})
        js_content = response.json()

        rag_content = ""
        for passage in js_content['relevant_passages']:
            print(passage['content'])
            rag_content += passage['content'] + "\n"  # 收集内容返回

        return rag_content

    def main(self):
        while True:
            user = input('你：')
            self.ask_q(user)

class My_Neuro(My_Rag):

    def __init__(self):
        super().__init__()

        API_KEY = 'sk-zk2674bb5f711d1a4662fc39a7cbc667f7f68589244066da'
        API_URL = 'https://api.zhizengzeng.com/v1'
        self.model = 'gemini-2.0-flash'
        self.messages = [{'role':'system','content':'你是一个傲娇的AI'}]

        self.WINDOW_SIZE = 30

        self.client = OpenAI(api_key=API_KEY,base_url=API_URL)

    def add_message(self,role,content):
        self.messages.append({
            'role':role,
            'content':content
        })

        #对话轮次超出WINDOW_SIZE上限则删除最开始的对话记录
        if len(self.messages) > self.WINDOW_SIZE:
            self.messages.pop(1)

    def get_requests(self):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            stream=True
        )

        return response

    def accept_content(self,response):

        full_assistant = ''
        print('AI:',end='')

        for chunk in response:
            if chunk.choices and chunk.choices[0].delta.content is not None:
                ai_response = chunk.choices[0].delta.content
                print(ai_response,end='',flush=True)

                full_assistant+=ai_response

        print()

        return full_assistant

    def start_chat(self):
        while True:
            user = input('你：')

            rag_content = self.ask_q(user)
            self.add_message('user',user+f'检索到关于{user}记忆请用合适的语气回应：{rag_content}')
            response = self.get_requests()
            ai_response = self.accept_content(response)
            self.add_message('assistant',ai_response)

my_neuro = My_Neuro()
my_neuro.start_chat()

