from fastapi import APIRouter
from query.filtering import routes as filtering
from query.summarization import routes as summarize
from query.question_answering import routes as qa
# Main router for querying
router = APIRouter()

router.include_router(summarize.router, prefix="/summarize")
router.include_router(qa.router, prefix="/question")
router.include_router(filtering.router, prefix="/filter")