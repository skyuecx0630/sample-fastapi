from fastapi import FastAPI, Response
from datetime import datetime

app = FastAPI()


@app.get("/")
def hello(http_res: Response):
    http_res.status_code = 200
    return "hello"


@app.get("/health")
def health(http_res: Response):
    http_res.status_code = 200
    return "OK"


@app.get("/now")
def now(http_res: Response):
    http_res.status_code = 200
    return str(datetime.now())
