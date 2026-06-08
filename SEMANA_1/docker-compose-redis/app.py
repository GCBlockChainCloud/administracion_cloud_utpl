from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379, decode_responses=True)

@app.route("/")
def inicio():
    visitas = redis.incr("visitas")
    return {
        "mensaje": "Hola desde Flask con Redis usando Docker Compose",
        "visitas": visitas,
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
