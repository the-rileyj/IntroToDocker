# Start a static NGINX webserver

```bash
docker run -v "$(pwd)/html:/usr/share/nginx/html" -p 5777:80 -d nginx
```

If using WSL, make sure you run this in Powershell (or somethings that has proper TTY interfacing)