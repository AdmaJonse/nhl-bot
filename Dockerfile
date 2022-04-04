FROM python:3.8-alpine

ENV STATIC_URL /static
ENV STATIC_PATH /bot/app/static

RUN mkdir /bot
ADD . /bot
WORKDIR /bot

RUN pip install -r requirements.txt

CMD ["python", "app.py"]