## Flask REST API

### How to build image:

- `docker build -t flask-rest-api .`

### How to run in docker (develop):

- `docker run -p 5000:5000 -w /app -v "$(pwd):/app" flask-rest-api sh -c "flask run --host 0.0.0.0"`

### How to run redis worker:

- `docker run -w /app flask-rest-api sh -c "rq worker -u REDIS_URL emails"`

### How to run in docker (production):

- `docker run -dp 5000:5000`

### Run DB migration

- `flask db migrate`
- `flask db upgrade`

### Run locally (no docker)

- `flask run`
