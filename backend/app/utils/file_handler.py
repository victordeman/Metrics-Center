from fastapi import UploadFile
import shutil

def handle_uploaded_file(file: UploadFile):
    path = f"uploads/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return path
