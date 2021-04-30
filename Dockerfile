FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /mypan
WORKDIR /mypan

RUN pip install pip -U -i https://pypi.tuna.tsinghua.edu.cn/simple

ADD . /mypan/

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
