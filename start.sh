#!/bin/bash
app="twitter-bot"
docker build -t ${app} .
docker run -d -p 5000:5000 --name=${app} -v $PWD:/bot ${app}