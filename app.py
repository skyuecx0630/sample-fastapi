import logging
from fastapi import FastAPI, Response
from datetime import datetime

logger = logging.getLogger('uvicorn')
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
    now = datetime.now()
    logger.info(str(now))
    return str(now)
