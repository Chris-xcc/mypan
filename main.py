from datetime import datetime

from fastapi import FastAPI, UploadFile, File  # Fastapi
from fastapi.middleware.cors import CORSMiddleware  # 跨域调用
from starlette.responses import FileResponse
from fastapi.responses import HTMLResponse
import uvicorn
import os


app = FastAPI()
origins = ['*']  # 或者 ['http://wicos.me'] 可以自定义允许访问的地址
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.post('/upload')
async def recv_file(file: UploadFile = File(...)):
    file_data = await file.read()
    with open('./file/' + file.filename, 'wb') as fp:
        fp.write(file_data)
    rt_msg = {
        'name': file.filename,
        'type': file.content_type
    }
    return rt_msg


@app.get("/download/{file_name}")
async def download(file_name: str):
    print(file_name)
    basedir = os.path.abspath(os.path.dirname(__file__))
    path = basedir + '\\' + str(datetime.now().date())
    file_path = basedir + '\\' + file_name + '.xlsx'
    print(file_path)
    return FileResponse(file_name)


@app.get("/")
async def main():
    os.chdir('file')
    print(os.getcwd())
    a = os.listdir(os.getcwd())
    print(a)
    msg = a
    content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset='UTF-8'>
    <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css">
</head>
<body>
    <div id='app'>
        <el-button @click='addFile'>addFile</el-button>
        <el-button @click='uploadFile'>uploadFile</el-button>
        <input type='file' ref='upload_input' style='display: none;' @change='select_file'>
    </div>
</body>
<script src='https://unpkg.com/vue/dist/vue.js'></script>
<script src='https://unpkg.com/element-ui/lib/index.js'></script>
<script src='https://cdn.bootcdn.net/ajax/libs/axios/0.19.2/axios.min.js'></script>
<script>
    new Vue({
        el: '#app',
        data: function () {
            return {
                select_file_data: '',
                target_url: 'http://127.0.0.1:8000/upload' // 上传文件的目标地址，即后台运行的暴露地址
            }
        },
        methods: {
            addFile: function () {
                this.$refs.upload_input.click () // 通过 ref 模拟点击
            },
            uploadFile: function () {
                let uploads = new FormData () // 创建 FormData
                let config = { headers: { 'Content-Type': 'multipart/form-data' } }
                if (this.select_file_data != '') {
                    uploads.append ('file',this.select_file_data [0]) // 此处只展示上传单个文件
                    axios.post(this.target_url, uploads, config).then(function (res) {
                        console.log(res.data)
                    })
                }
            },
            select_file: function (file) {
                this.select_file_data = file.target.files
                console.log(this.select_file_data)
            }
        }
    })
</script>
</html>
    """
    return HTMLResponse(content=content)
    # return {'file': msg}
