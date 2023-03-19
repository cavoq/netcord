# netcord
Discord bot to perform network operations through discord.

![license](https://img.shields.io/badge/license-MIT-brightgreen.svg)
![version](https://img.shields.io/badge/version-1.0.0-lightgrey.svg)

## Supported commands

- *!ping* <host> Ping a host
- *!trace <host>* Trace a host
- *!locate <host>* Get a map of the approximate location of a host

## Setup

Create a file called .env and fill it with the following information:
```
CONFIG_FILE=config.json
DISCORD_TOKEN=<YOUR_DISCORD_TOKEN>
```

## Usage

See *make help*

![image](https://user-images.githubusercontent.com/61215846/226197305-84e6ea1e-f929-4430-9072-ddfb60da268c.png)

## Deployment

The easiest way is to deploy on https://console.qovery.com.

You can also deploy on your own server by running the following commands:
```
make build && make run
```
