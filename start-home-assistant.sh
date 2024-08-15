#!/bin/bash

docker start homeassistant

echo "Started on localhost:8123"

#docker run \
#  --name homeassistant \
#  --privileged \
#  --restart=unless-stopped \
#  -e TZ=Europe/Berlin \
#  -v ./home-assistant-config:/config \
#  -v /run/dbus:/run/dbus:ro \
#  --network=host \
#  ghcr.io/home-assistant/home-assistant:stable
