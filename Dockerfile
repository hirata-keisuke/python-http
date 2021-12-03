# サーバに来たリクエストに対して個別の処理を実装するには
# http.server.BaseHTTPRequestHandlerを継承したクラスを使う
FROM python:3.7-alpine

EXPOSE 8000/tcp

COPY ./server.py /server.py
COPY ./index.html /index.html

CMD ["python", "server.py"]
