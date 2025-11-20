from fastapi import APIRouter, UploadFile, File

from app.file_converter.fc import file_converter

router = APIRouter()

@router.post('/convert-to-pdf',response_model=None)
async def a(office_files: list[UploadFile] = File(...)):
    return await file_converter(office_files)
