from flask import Blueprint, jsonify, render_template_string
import socket
from .pokeneas import random_pokenea, POKENEAS  # ⬅️ Importamos la lista completa

bp = Blueprint('main', __name__)

def get_container_id():
    return socket.gethostname()

# 🔹 Ruta 1 (ya existente): un Pokenea aleatorio (JSON)
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

# 🔹 Ruta 2 (ya existente): un Pokenea aleatorio (HTML)
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

# 🔹 NUEVA Ruta 3: todos los Pokeneas (JSON)
@bp.route('/api/pokeneas')
def api_all_pokeneas():
    data = []
    for p in POKENEAS:
        data.append({
            "id": p["id"],
            "nombre": p["nombre"],
            "altura": p["altura"],
            "habilidad": p["habilidad"],
            "container_id": get_container_id()
        })
    return jsonify(data)

# 🔹 NUEVA Ruta 4: todos los Pokeneas (HTML)
@bp.route('/show/pokeneas')
def show_all_pokeneas():
    container_id = get_container_id()
    html = """
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Pokeneas - Todos</title>
        <style>
          body { font-family: Arial, sans-serif; background:#f7f7f7; text-align:center; padding:30px; }
          .grid { display: flex; flex-wrap: wrap; justify-content: center; }
          .card {
            background: white; margin:10px; padding:15px; border-radius:10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1); width:220px;
          }
          .card img { width:100%; border-radius:8px; }
          .small { color:#666; font-size:0.8rem; }
        </style>
      </head>
      <body>
        <h1>Pokeneas en el contenedor {{ container_id }}</h1>
        <div class="grid">
          {% for p in pokeneas %}
          <div class="card">
            <h3>{{ p.nombre }}</h3>
            <img src="{{ p.imagen }}" alt="{{ p.nombre }}">
            <p><strong>Habilidad:</strong> {{ p.habilidad }}</p>
            <p><em>"{{ p.frase }}"</em></p>
          </div>
          {% endfor %}
        </div>
      </body>
    </html>
    """
    return render_template_string(html, pokeneas=POKENEAS, container_id=container_id)
