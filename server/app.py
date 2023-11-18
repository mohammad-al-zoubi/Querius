from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from backend.QA.main import LogQA
from server.query import routes as query
from server.authentication import routes as auth
from server.utils import dummy_answer
from server.logs import routes as logs

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

# uvicorn main:app --reload

# include routes to the multiple services
app.include_router(auth.router, prefix="/auth")
app.include_router(logs.router, prefix="/log")
app.include_router(query.router, prefix="/query")


@app.post("/query", tags=["query"])
def query():
    return dummy_answer()


@app.get("/", tags=["root"])
def root():
    return {"status": "up and running"}


@app.get("/test", tags=["test"])
def test():
    from backend.QA.main import test
    test()