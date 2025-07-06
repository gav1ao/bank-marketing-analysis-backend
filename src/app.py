import logging

from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info

from src.logger import setup as settup_logging
from src.routes import register_routes

settup_logging()

log = logging.getLogger(__name__)


def create_app():
    info = Info(title="Bank Marketing Analysis API", version="1.0.0")
    app = OpenAPI(__name__, info=info)
    CORS(app)

    register_routes(app)

    return app
