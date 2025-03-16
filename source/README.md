# Running This Challenge

Build
```
docker build -t athack-ctf/chall2025-apocalypse:latest .
```

Run
```
docker run -d --name apocalypse \
  -p 52042:80 \
  athack-ctf/chall2025-apocalypse:latest
```
