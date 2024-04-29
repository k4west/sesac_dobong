from pydantic import BaseModel


class UpperRequest(BaseModel):
    msg: str
