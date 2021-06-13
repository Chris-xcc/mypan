##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Phenix-G
# @File   : main.py
# @Time   : 2021/06/04 00:19:05
import os
from pathlib import Path
from typing import List

from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware  # 跨域调用
from fastapi.responses import RedirectResponse, FileResponse
from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
# origins = ['*']  # 或者 ['http://wicos.me'] 可以自定义允许访问的地址
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*'],
# )
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")

BASE_DIR = Path(__file__).resolve().parent
VIRUS_EXTENSION_NAME = [
    'exe', 'scr', 'com', 'vb', 'vbs', 'js', 'VBS',
    'VBE', 'JS', 'JSE', 'WSH', 'WSF', 'bat', 'sh', 'inf'
]
VIRUS = [virus for virus in map(lambda x: '.' + x, VIRUS_EXTENSION_NAME)]

FILE_PATH = BASE_DIR.joinpath('file')
TemplateResponse = templates.TemplateResponse


def get_files():
    files = [os.path.basename(str(path)) for path in FILE_PATH.iterdir()]
    yield files


def write_file(file):
    with open('./file/{}'.format(file.filename), 'wb')as f:
        for i in iter(lambda: file.file.read(1024 * 1024 * 10), b''):
            f.write(i)


@app.post("/uploadfile/")
async def upload(request: Request, files: List[UploadFile] = File(...)):
    for file in files:
        if file.filename:
            extension_name = Path(file.filename).suffix
            if extension_name in VIRUS:
                return TemplateResponse('index.html', {'request': request, 'files': get_files(), 'fail': '上传失败'})
            else:
                write_file(file)
        else:
            return RedirectResponse('http://127.0.0.1:8000/')
    return TemplateResponse('index.html', {'request': request, 'files': get_files(), 'success': '上传成功'})


@app.get("/download/{file_name}")
async def download(file_name: str) -> FileResponse:
    path = str(FILE_PATH.joinpath(file_name))
    return FileResponse(path)


@app.get("/")
async def index(request: Request) -> TemplateResponse:
    return TemplateResponse('index.html', {'request': request, 'files': get_files()})


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', port=8000, debug=True, reload=True)
