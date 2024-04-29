import gradio as gr
import time

from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel

tokenizer = PreTrainedTokenizerFast.from_pretrained(
    "skt/kogpt2-base-v2",
    bos_token="</s>",
    eos_token="</s>",
    unk_token="<unk>",
    pad_token="<pad>",
    mask_token="<mask>",
)
model = GPT2LMHeadModel.from_pretrained("skt/kogpt2-base-v2")


def answer(text, history):
    input_ids = tokenizer.encode(text, return_tensors="pt")
    gen_ids = model.generate(
        input_ids,
        max_length=128,
        repetition_penalty=2.0,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
        bos_token_id=tokenizer.bos_token_id,
        use_cache=True,
    )
    generated = tokenizer.decode(gen_ids[0])
    return generated


app = gr.ChatInterface(answer)
app.launch(server_name="0.0.0.0")

# def make_upper(msg, progress=gr.Progress()):
#     progress(0, desc="Starting")
#     time.sleep(1)
#     progress(0.25)
#     time.sleep(1)
#     progress(0.5)
#     time.sleep(1)
#     progress(0.75)
#     time.sleep(1)
#     progress(1)

#     return msg.upper()


# app = gr.Interface(make_upper, inputs=["text"], outputs=["text"])
