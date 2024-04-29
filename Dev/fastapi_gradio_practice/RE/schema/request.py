from pydantic import BaseModel


class UpperRequest(BaseModel):
    msg: str


class PostGeneration(BaseModel):
    msg: str


class PostSummarization(BaseModel):
    msg: str
