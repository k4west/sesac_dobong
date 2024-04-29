from fastapi import FastAPI
from api import sesac, ocr

app = FastAPI()
app.include_router(sesac.router)
app.include_router(ocr.router)


@app.get("/")
def haelth_check_handler():
    return {"ping": "pong"}
