from fastapi import FastAPI
from summarization import routes as summarize
from question_answering import routes as qa
from filtering import routes as filtering
from authentication import routes as auth
from utils import generate_random_id

app = FastAPI()

# uvicorn main:app --reload

# include routes to the multiple services
app.include_router(summarize.router, prefix="/summarize")
app.include_router(qa.router, prefix="/question")
app.include_router(filtering.router, prefix="/filter")
app.include_router(auth.router, prefix="/auth")

