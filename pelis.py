from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from movies.db import get_db

bp = Blueprint('pelis', __name__)

@bp.route('/')
def index():
    db = get_db()
    pelis = db.execute(
        """SELECT l.name AS lenguaje, f.title AS titulo, release_year AS Año
           FROM language l JOIN film f ON l.language_id = f.language_id
           ORDER BY name ASC"""

        """SELECT title AS Película, first_name AS Nombre, last_name AS Apellido
            FROM actor a JOIN film_actor fa ON a.actor_id = fa.actor_id
            JOIN film f ON fa.film_id = f.film_id
            ORDER BY Película ASC"""

        """SELECT c.name AS categoria, title AS Pelicula
            FROM category c JOIN film_category fc ON c.category_id = fc.category_id
            JOIN film f ON fc.film_id = f.film_id
            ORDER BY Pelicula ASC"""
    ).fetchall()
    return render_template('pelis/index.html', pelis=pelis)