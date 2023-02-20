FROM python:3.8

WORKDIR /words-in-songs

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV HOST=redis
ENV PORT=6379
ENV DB=0

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
