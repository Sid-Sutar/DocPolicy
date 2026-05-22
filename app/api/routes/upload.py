from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from sqlalchemy.orm import Session

import os
import shutil
import uuid

from app.database.database import get_db
from app.models.contract import Contract

from app.core.logger import logger

router = APIRouter()

UPLOAD_FOLDER = "data/contracts"

@router.post("/upload-contract")
def upload_contract(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    try:

        logger.info(
            f"Uploading contract: {file.filename}"
        )

        # Validate PDF
        if not file.filename.endswith(".pdf"):

            logger.warning(
                "Invalid file type uploaded"
            )

            return {
                "success": False,
                "error": "Only PDF files are allowed"
            }

        # Generate unique filename
        unique_filename = (
            f"{uuid.uuid4()}.pdf"
        )

        file_path = os.path.join(
            UPLOAD_FOLDER,
            unique_filename
        )

        # Save file
        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        # Save metadata to database
        contract = Contract(
            filename=file.filename,
            stored_filename=unique_filename,
            file_path=file_path
        )

        db.add(contract)
        db.commit()
        db.refresh(contract)

        logger.info(
            f"Contract uploaded successfully: "
            f"{unique_filename}"
        )

        return {
            "success": True,
            "message": "Contract uploaded successfully",
            "contract_id": contract.id,
            "filename": file.filename,
            "stored_filename": unique_filename
        }

    except Exception as e:

        logger.error(
            f"Upload failed: {str(e)}"
        )

        return {
            "success": False,
            "error": str(e)
        }
