import gradio as gr

import torch
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration

tokenizer = PreTrainedTokenizerFast.from_pretrained("gogamza/kobart-summarization")
model = BartForConditionalGeneration.from_pretrained(
    "gogamza/kobart-summarization", max_length=256
)


def make_summary(text, history):
    raw_input_ids = tokenizer.encode(text)
    input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]

    summary_ids = model.generate(torch.tensor([input_ids]))
    generated = tokenizer.decode(
        summary_ids.squeeze().tolist(), skip_special_tokens=True
    )
    return generated


app = gr.ChatInterface(make_summary)
app.launch(share=True)
