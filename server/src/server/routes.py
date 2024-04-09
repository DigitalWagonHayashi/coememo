from fastapi import UploadFile, File, FastAPI
from starlette.responses import JSONResponse
from uuid import uuid4

from src.db.crud import save_voice as save_voice_db
from src.util.const import voice_storage_path


app = FastAPI()


@app.post("/upload/voice")
async def save_voice(file: UploadFile = File(...)):
    if file.content_type != "audio/mpeg":
        return JSONResponse(content={"error": "Invalid file type. Only mp3 files are allowed."}, status_code=400)

    file_path = voice_storage_path / (str(uuid4())+'.mp3')
    # ファイルを保存
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # dbに保存
    saved_id = save_voice_db(str(file_path), "machine_id")
    return JSONResponse(content={"id": saved_id})
