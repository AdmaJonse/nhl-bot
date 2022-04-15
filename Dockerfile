FROM python:3.8-alpine

RUN mkdir /bot
ADD . /bot
WORKDIR /bot

RUN pip install -r requirements.txt

CMD ["python", "app.py"]