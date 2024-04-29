from fastapi import APIRouter
from schema.request import UpperRequest

router = APIRouter(prefix="/sesac")


# post 대문자로 바꿔주는 API
@router.post("/upper")
def uppercase(request: UpperRequest):
    result = request.msg.upper()
    return {"result": result}
