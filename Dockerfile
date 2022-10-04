FROM python:3.8-alpine

ENV PORT=${PORT:-8080}
EXPOSE $PORT

RUN mkdir /bot
ADD . /bot
WORKDIR /bot

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
