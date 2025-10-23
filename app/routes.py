from flask import Blueprint, jsonify, render_template_string
import socket
from .pokeneas import random_pokenea

bp = Blueprint('main', __name__)

def get_container_id():
    # en Docker, el hostname es el id del contenedor
    return socket.gethostname()

@bp.route('/api/pokenea')
def api_pokenea():
    p = random_pokenea()
    data = {
        "id": p["id"],
        "nombre": p["nombre"],
        "altura": p["altura"],
        "habilidad": p["habilidad"],
        "container_id": get_container_id()
    }
    return jsonify(data)

@bp.route('/show/pokenea')
def show_pokenea():
    p = random_pokenea()
    container_id = get_container_id()
    html = """
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Pokenea - {{ nombre }}</title>
        <style>
          body { font-family: Arial, sans-serif; text-align:center; padding:30px; }
          img { max-width: 300px; height: auto; border-radius: 10px; }
          .card { display:inline-block; padding:20px; border-radius:10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
          .small { color: #666; font-size: 0.9rem; }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>{{ nombre }}</h1>
          <img src="{{ imagen }}" alt="{{ nombre }}">
          <p><em>"{{ frase }}"</em></p>
          <p class="small">Contenedor: {{ container_id }}</p>
        </div>
      </body>
    </html>
    """
    return render_template_string(html,
                                  nombre=p["nombre"],
                                  imagen=p["imagen"],
                                  frase=p["frase"],
                                  container_id=container_id)
