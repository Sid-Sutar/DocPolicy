from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

import os
import shutil
import uuid

from app.database.database import get_db
from app.models.contract import Contract

router = APIRouter()

UPLOAD_FOLDER = "data/contracts"

@router.post("/upload-contract")
def upload_contract(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    # Validate PDF
    if not file.filename.endswith(".pdf"):
        return {
            "error": "Only PDF files are allowed"
        }

    # Generate unique filename
    unique_filename = f"{uuid.uuid4()}.pdf"

    file_path = os.path.join(
        UPLOAD_FOLDER,
        unique_filename
    )

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Save metadata to DB
    contract = Contract(
        filename=file.filename,
        stored_filename=unique_filename,
        file_path=file_path
    )

    db.add(contract)
    db.commit()

    return {
        "message": "Contract uploaded successfully",
        "filename": file.filename,
        "stored_filename": unique_filename
    }
