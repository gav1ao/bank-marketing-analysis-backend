import logging

from flask import jsonify, redirect
from flask_openapi3 import Tag
from werkzeug.exceptions import HTTPException

from src.schemas import BankClientSchema, BankDomainSchema, InternalServerErrorSchema
from src.schemas.prediction_result import PredictionResultSchema
from src.services.domain_service import BankDomainService
from src.services.prediction_service import PredictionService

log = logging.getLogger(__name__)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")


def register_routes(app):
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        """Retorna JSON ao invés de HTML para erros HTTP padrão (ex: 409, 404)."""
        response = e.get_response()
        response.data = jsonify({
            "error": e.name,
            "message": e.description,
            "status_code": e.code
        }).data
        response.content_type = "application/json"
        log.error(e)
        return response

    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e),
            "status_code": 500
        }), 500

    @app.get("/", tags=[home_tag])
    def home():
        """
        Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
        """
        return redirect("/openapi")

    @app.get("/domain", responses={"200": BankDomainSchema, "500": InternalServerErrorSchema})
    def get_domain():
        """
        Retorna os dados de domínio úteis para a predição do modelo.
        """
        bank_domain_service = BankDomainService()

        return jsonify(bank_domain_service.get_domain().model_dump())

    @app.post("/predict_offer", responses={"200": PredictionResultSchema, "500": InternalServerErrorSchema})
    def predict_offer(body: BankClientSchema):
        """
        Permite efetuar a predição se um cliente irá aderir a uma oferta ou não.
        """
        prediction_service = PredictionService()
        will_accept_offer = prediction_service.predict(body)

        return jsonify(PredictionResultSchema(will_accept_offer=will_accept_offer).model_dump())
