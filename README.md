## Flask REST API

### How to build image:

- `docker build -t flask-rest-api .`

### How to run in docker (develop):

- `docker run -p 5000:5000 -w /app -v "$(pwd):/app" flask-rest-api`

### How to run in docker (production):

- `docker run -dp 5000:5000`
