from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from appeliculas.db import get_db

bp = Blueprint('pelis', __name__,url_prefix="/pelis/")



@bp.route('/')
def index():
    db = get_db()
    peliculas = db.execute(
       
""" SELECT f.title as pelicula, f.film_id FROM film f
            join film_actor fa on f.film_id = fa.film_id 
            join actor a on fa.actor_id = a.actor_id
            WHERE a.actor_id = ?"""  
    ).fetchall()
    return render_template('pelis/.html', peliculas=peliculas)
    

