from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from ibm_watson import ApiException
import time
from . import service as service
from .. import config
import shutil

print('dddddddddd')
print(config.FRONTEND_URL, flush=True)

router = APIRouter()

@router.get('/health')
def health_check():
    print("message", flush=True)
    return JSONResponse(status_code=200, content={"status": "OK"})


@router.post('/upload')
async def upload_file(audio_file: UploadFile = File(...)):

    print("BACKEND", flush=True)

    # dummy = ['ご住所 の 変更 で ございます ね ご連絡 ありがとう ございます ', '〇 ます が ご契約 内容 確認 いたし ます ので お電話 いただいて いる 方 は 契約者 ご本人 様 で いらっしゃいます か ', 'はい そうです 本人 です ', 'それでは お電話 を いただいて おります お客様 の お名前 を お願い いたし ます ', '山田 太郎 です ', '山田 太郎 様 で いらっしゃいます ね ', 'では 契約者 ご本人 様 確認 のため 恐れ入ります が 山田 様 の 生年月日 を お願い いたし ます ', 'はい 生年月日 が 千 九百 三十 七年 六月 十 七 日 です ']
    # time.sleep(3)
    # return dummy
    if audio_file.content_type != config.CONTENT_TYPE:
        print(audio_file.content_type, flush=True)
        return JSONResponse(status_code=400, content={f'message": "Content type is not valid. Only {config.CONTENT_TYPE} is valid.'})

    path = f'{config.FILE_PATH}{audio_file.filename}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(audio_file.file, buffer)

    try:
        print("***** Calling Watoson speech to text API *****", flush=True)        
        return await service.call(audio_file)
    except ApiException as ex:
        print(f'Method failed with status code {str(ex.code)} : {ex.message}')
        return JSONResponse(status_code=ex.code, content={"message": ex.message})