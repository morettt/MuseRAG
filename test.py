import requests
import json

# 你的服务地址
url = "http://127.0.0.1:8002/ask"

def ask_q(ask,qty=1):
    response = requests.post(url, json={"question": ask, "top_k":qty})
    js_content = response.json()

    for passage in js_content['relevant_passages']:
        print(passage['content'])

def main():
    while True:
        user = input('你：')
        ask_q(user)

if __name__ == '__main__':
    main()