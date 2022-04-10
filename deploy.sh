#!/bin/bash

#
#  Description:
#    This script will build and deploy the docker image to Azure. 
#    The Docker service must be running on the machine already for
#    this script to function correctly.
#

app="avalanchebot"
resource_group="bot-resource-group"
registry="${app}.azurecr.io"
tag="${registry}/${app}:latest"

# build and push the updated docker container
docker build . -t ${app}
docker tag ${app} ${tag}
docker push ${tag}

# restart the webapp so that it will use the updated image
az webapp restart --name ${app} --resource-group ${resource_group}