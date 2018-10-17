# Webscraper Notes

## Info

https://github.com/SeleniumHQ/docker-selenium

docker run --rm --name godl -p 4444:4444 -v "$(pwd)\DummyDownload:/app/dl" selenium/standalone-chrome:3.14.0-helium

docker exec -it godl /bin/bash

find -name "lesson*"