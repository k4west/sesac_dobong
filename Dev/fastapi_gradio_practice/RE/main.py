from fastapi import FastAPI
from api import sesac, nlp


app = FastAPI()
app.include_router(sesac.router)
app.include_router(nlp.router)


@app.get("/")
def health_check_handler():
    return {"msg": "Hello World!"}
