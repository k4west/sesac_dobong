from fastapi import APIRouter
from schema.request import UpperRequest

router = APIRouter()


@router.post("/upper")
def change_upper_string_handler(request: UpperRequest):
    result = request.msg.upper()
    return {"result": result}
