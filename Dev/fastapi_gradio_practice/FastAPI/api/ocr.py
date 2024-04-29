from fastapi import File, UploadFile, APIRouter, HTTPException
from fastapi.responses import JSONResponse
import easyocr
from io import BytesIO
from typing import List
from PIL import Image
import numpy as np

router = APIRouter()

# 여기서 사용할 언어를 정의합니다. 예시에서는 영어('en')를 사용합니다.
reader = easyocr.Reader(["ko"])


@router.post("/process-image/")
async def process_image(file: UploadFile = File(...)) -> JSONResponse:
    if not file.filename.endswith((".png", ".jpg", ".jpeg")):
        return JSONResponse(status_code=400, content={"message": "Invalid file format"})
        # raise HTTPException(status_code=400, detail="Invalid file format")

    contents = await file.read()
    image = Image.open(BytesIO(contents))
    image_np = np.array(image)
    results = reader.readtext(image_np)
    print(results)
    # 결과 포맷팅
    text_results = ""
    for bbox, text, prob in results:
        text_results += text + " "

    return JSONResponse(status_code=200, content={"results": text_results})
