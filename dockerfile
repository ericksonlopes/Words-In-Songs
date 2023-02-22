FROM python:3.8

WORKDIR /words-in-songs

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV REDIS_HOST=redis
ENV REDIS_PORT=6379
ENV REDIS_DB=0

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
