   from . import peliculas
    app.register_blueprint(peliculas.bp)
    app.add_url_rule('/', endpoint='index')


    from . import category
    app.register_blueprint(category.bp)


    from . import language
    app.register_blueprint(language.bp)


    return app