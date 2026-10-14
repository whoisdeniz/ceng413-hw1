"""Tiny demo web service for the Week 4 Docker lab.

Endpoints
  GET /health        -> {"status": "ok"}            (stateless)
  GET /greet?name=X  -> {"message": "Hello, X!"}    (stateless)
  GET /visit         -> {"visits": N}               (STATEFUL on purpose:
                        the counter is stored in a file so we can see what
                        happens to data when a container is removed)

Configuration comes from environment variables (12-factor style):
  APP_GREETING  default "Hello"
  DATA_DIR      default "/data"   (where the visit counter file lives)
"""
import os
from pathlib import Path
import random

from flask import Flask, jsonify, request

app = Flask(__name__)

GREETING = os.environ.get("APP_GREETING", "Hello")
DATA_DIR = Path(os.environ.get("DATA_DIR", "/data"))


def _counter_file() -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR / "visits.txt"


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/info")
def info():
    return jsonify(
        app="ceng413-hw1",
        version="1.0",
        framework="Flask"
    )


@app.get("/motivation")
def motivation():
    messages = [
        "Bugün harika şeyler başarabilirsin! ✨",
        "Kendine inan, düşündüğünden daha güçlüsün. 💛",
        "Küçük adımlar da seni ileriye götürür. 🌱",
        "Her yeni gün yeni bir başlangıçtır. ☀️",
        "Kendi hızında ilerlemen de ilerlemektir. 🌷",
        "Bugün kendine biraz daha nazik davran. 🫶",
        "Hayallerin için attığın her adım değerlidir. 🌟",
        "Her şeyi bugün çözmek zorunda değilsin. 🍀",
        "Başlamak için mükemmel olmak zorunda değilsin. 🚀",
        "Güzel şeyler bazen hiç beklemediğin anda gelir. 🌈",
        "Kendinle gurur duymak için küçük bir neden bul. 💖",
        "Bugün yeni bir şey öğrenmek için harika bir gün. 📚",
    ]

    return jsonify(message=random.choice(messages))



@app.get("/greet")
def greet():
    name = request.args.get("name", "world")
    return jsonify(message=f"{GREETING}, {name}!")


@app.get("/visit")
def visit():
    f = _counter_file()
    current = int(f.read_text()) if f.exists() else 0
    current += 1
    f.write_text(str(current))
    return jsonify(visits=current)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
