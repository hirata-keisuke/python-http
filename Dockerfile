# サーバの起動をスクリプトに書く第一歩
FROM python:3.7-alpine

EXPOSE 8000/tcp

COPY ./server.py /server.py
COPY ./index.html /index.html

CMD ["python", "server.py"]
