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

## How to deploy the application to Azure

1. Build the docker container:
```
docker build . -t avalanchebot
```

2. Tag the docker container:
```
docker tag avalanchebot avalanchebot.azurecr.io/avalanchebot:latest
```

3. Push the docker container to the Azure container repository:
```
docker push avalanchebot.azurecr.io/avalanchebot:latest
```

4. Restart the Azure webapp.
```
az webapp restart --name avalanchebot --resource-group bot-resource-group
```