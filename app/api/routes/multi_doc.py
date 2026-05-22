from fastapi import APIRouter

from app.services.multi_doc_service import (
    multi_document_query
)

router = APIRouter()

@router.get("/multi-document-query")
def run_multi_document_query(
    query: str
):

    result = multi_document_query(
        query
    )

    return result

