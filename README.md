# nhl-bot
A Twitter bot that posts when events occur in Colorado Avalanche games.

This seemed like a fun way to learn about the Twitter and NHL APIs. The bot is still a work-in-progress and provides very simple event updates.

## How to build and run the docker container locally

1. Build the docker container:
```
docker build -t twitter-bot .
```

2. Run the docker container:
```
docker run -it twitter-bot
```

## How to deploy the application to heroku

1. Build the image and push to container registry:
```
heroku container:push web
```

2. Release the image:
```
heroku container:release web
```
