import os
import json
import requests
import gradio as gr

BACKEND_URL = "http://172.16.219.147:8000/nlp"


def gen(text, history):
    payload = {"msg": text}
    response = requests.post(BACKEND_URL + "/generation", data=json.dumps(payload))
    generated = response.json()["result"]
    return generated


def sum(text, history):
    payload = {"msg": text}
    response = requests.post(BACKEND_URL + "/summarization", data=json.dumps(payload))
    generated = response.json()["result"]
    return generated


def answer(text, history):
    fn, text = text[:2], text[2:]
    if fn == "요약":
        return sum(text, history)
    else:
        return gen(text, history)


demo = gr.ChatInterface(
    answer, description="생성 또는 요약을 먼저 작성하시고 뒤에 문장을 작성해주세요!"
)
# demo = gr.TabbedInterface(
#     [gr.ChatInterface(sum), gr.ChatInterface(gen)], tab_names=["summary", "generation"]
# )
demo.launch(share=True)
