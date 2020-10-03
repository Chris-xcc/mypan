from fastapi import FastAPI, UploadFile, File  # Fastapi
from fastapi.middleware.cors import CORSMiddleware  # 跨域调用
from starlette.requests import Request
from starlette.responses import FileResponse, RedirectResponse
from starlette.templating import Jinja2Templates
import uvicorn
import os

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


def get_files():
    os.chdir('file')
    files = os.listdir(os.getcwd())
    os.chdir('..')
    return files


@app.post("/uploadfile/")
async def upload(request: Request, file: UploadFile = File(...)):
    print(file.filename)
    if file.filename:
        viruses = ['exe', 'scr', 'com', 'vb', 'vbs', 'js', 'VBS', 'VBE', 'JS', 'JSE', 'WSH', 'WSF']
        # print(file.filename)
        extension_name = os.path.splitext(file.filename)[-1]
        if extension_name in viruses:
            return templates.TemplateResponse('index.html', {'request': request, 'fail': '上传失败'})
        else:
            files = get_files()
            file_data = await file.read()
            with open('./file/' + file.filename, 'wb')as f:
                f.write(file_data)
            files.append(file.filename)
            return templates.TemplateResponse('index.html', {'request': request, 'files': files, 'success': '上传成功'})
    else:
        return RedirectResponse('http://127.0.0.1:8000/')


@app.get("/download/{file_name}")
def download(file_name: str):
    basedir = os.path.abspath(os.path.dirname(__file__))
    path = basedir + r'/file/' + file_name
    return FileResponse(path)


@app.get("/")
async def index(request: Request):
    files = get_files()
    return templates.TemplateResponse('index.html', {'request': request, 'files': files})


if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000)
