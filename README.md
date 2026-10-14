# CENG413 HW-1
Build: `docker build -t ceng413-hw1:v1 .`
Run: `docker run --rm -p 8000:8000 -e APP_GREETING=Hello ceng413-hw1:v1`
Endpoints: `http://localhost:8000/health`, `http://localhost:8000/greet?name=Ada`, `http://localhost:8000/visit`
Custom endpoints: `http://localhost:8000/info`, `http://localhost:8000/motivation`