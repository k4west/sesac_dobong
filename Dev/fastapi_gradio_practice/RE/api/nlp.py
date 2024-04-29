from fastapi import APIRouter
from schema.request import PostGeneration, PostSummarization

import torch
from transformers import (
    PreTrainedTokenizerFast,
    GPT2LMHeadModel,
    BartForConditionalGeneration,
)

router = APIRouter(prefix="/nlp")

gen_tokenizer = PreTrainedTokenizerFast.from_pretrained(
    "skt/kogpt2-base-v2",
    bos_token="</s>",
    eos_token="</s>",
    unk_token="<unk>",
    pad_token="<pad>",
    mask_token="<mask>",
)
gen_model = GPT2LMHeadModel.from_pretrained("skt/kogpt2-base-v2")
sum_tokenizer = PreTrainedTokenizerFast.from_pretrained("gogamza/kobart-summarization")
sum_model = BartForConditionalGeneration.from_pretrained(
    "gogamza/kobart-summarization", max_length=256
)


@router.post("/generation")
def gen_txt(request: PostGeneration):
    input_ids = gen_tokenizer.encode(request.msg, return_tensors="pt")
    gen_ids = gen_model.generate(
        input_ids,
        max_length=256,
        repetition_penalty=2.0,
        pad_token_id=gen_tokenizer.pad_token_id,
        eos_token_id=gen_tokenizer.eos_token_id,
        bos_token_id=gen_tokenizer.bos_token_id,
        use_cache=True,
    )
    generated = gen_tokenizer.decode(gen_ids[0])
    return {"result": generated}


@router.post("/summarization")
def sum__txt(request: PostSummarization):
    raw_input_ids = sum_tokenizer.encode(request.msg)
    input_ids = (
        [sum_tokenizer.bos_token_id] + raw_input_ids + [sum_tokenizer.eos_token_id]
    )

    summary_ids = sum_model.generate(torch.tensor([input_ids]))
    summarized = sum_tokenizer.decode(
        summary_ids.squeeze().tolist(), skip_special_tokens=True
    )
    return {"result": summarized}
