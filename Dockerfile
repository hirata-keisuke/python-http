# 最も簡単、サーバとして起動するだけ
FROM python:3.7-alpine

EXPOSE 8000/tcp

CMD ["python", "-m", "http.server", "8000"]
