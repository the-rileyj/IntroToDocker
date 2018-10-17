# Compile Notes

## Info

### Build image to be pushed, then push image

#### Syntax

Build a local image and tag it:

```bash
~/DOCKERPRESENTATION/SIMPLECOMPILATION/DOCKERFILED $ docker build -t {username}/{image name}:{tag, usually: latest} {path to directory with dockerfile}
```

Push built and tagged image to registry (default is hub.docker.com)

```bash
~/DOCKERPRESENTATION/SIMPLECOMPILATION/DOCKERFILED $ docker push {username}/{image name}:{tag, usually: latest}
```

#### Examples

```bash
~/DOCKERPRESENTATION/SIMPLECOMPILATION/DOCKERFILED $ docker build -t therileyjohnson/compile-me:latest .
```

```bash
~/DOCKERPRESENTATION/SIMPLECOMPILATION/DOCKERFILED $ docker push therileyjohnson/compile-me:latest
```