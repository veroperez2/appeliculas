
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from appeliculas.db import get_db

bp = Blueprint('pelis', __name__,url_prefix="/actor/")

@bp.route('/<int:id>/', methods=('GET', 'POST'))
def update(id):
     db = get_db()
     actores = db.execute(
        """ SELECT f.film_id, f.title FROM film f
         SELECT a.actor_id, first_name as nombre, last_name as apellido 
            FROM actor a ORDER BY apellido, nombre"""
    ).fetchall()

     return render_template('blog/update.html', post=post)


def index():
    db = get_db()
    actores = db.execute(
        """ SELECT f.film_id, f.title FROM film f
         SELECT a.actor_id, first_name as nombre, last_name as apellido 
            FROM actor a ORDER BY apellido, nombre"""
    ).fetchall()
    return render_template('actor/index.html', actores = actores)

@bp.route('/<int:id>')
def get_actor(id):
    peliculas = get_db().execute(
       """ SELECT f.title as pelicula, f.film_id FROM film f
            join film_actor fa on f.film_id = fa.film_id 
            join actor a on fa.actor_id = a.actor_id
            WHERE a.actor_id = ?"""
    ).fetchall()
    
    actor = get_db().execute(
       """ SELECT a.actor_id, first_name as nombre, last_name as apellido FROM actor a 
            WHERE a.actor_id = ? """,(id,)).fetchone()
    return render_template('actor/detalle.html', peliculas = peliculas, actor = actor)