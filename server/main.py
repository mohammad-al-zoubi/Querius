from fastapi import FastAPI
from query.summarization import routes as summarize
from query.question_answering import routes as qa
from query import routes as query
from authentication import routes as auth
from utils import dummy_answer
from logs import routes as logs

app = FastAPI()

# uvicorn main:app --reload

# include routes to the multiple services
app.include_router(auth.router, prefix="/auth")
app.include_router(logs.router, prefix="/log")
app.include_router(query.router, prefix="/query")


@app.post("/query")
def query():

    return dummy_answer()


