from flask import Flask
from .views import view
from .filters import _slice
from .database import Database

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        app.register_blueprint(view, url_prefix="/")

        @app.context_processor
        def slice():
            return dict(slice=_slice)

        return app
