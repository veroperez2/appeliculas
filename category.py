from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from appeliculas.db import get_db

bp = Blueprint('category', __name__,url_prefix="/category/")

@bp.route('/')
def index():
    db = get_db()
    category = db.execute(
        """SELECT c.name AS categorias FROM category c """
    ).fetchall()
    return render_template('category/index.html', category = category)