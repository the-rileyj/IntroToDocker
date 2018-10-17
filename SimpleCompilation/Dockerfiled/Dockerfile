FROM golang:1.11.1-alpine3.8

WORKDIR /app/src/

COPY CompileMe.go .

RUN go build -o CompileMe CompileMe.go

ENTRYPOINT "./CompileMe"