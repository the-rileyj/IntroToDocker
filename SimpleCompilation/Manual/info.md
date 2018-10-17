# Compile Notes

## Info

docker run --rm -it -v "$(pwd):/app/comp" golang:1.11.1-alpine3.8" /bin/sh

GOOS=windows GOARCH=amd64

go build -o CompileMe.exe CompileMe.go