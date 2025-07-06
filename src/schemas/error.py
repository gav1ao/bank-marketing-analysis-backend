from pydantic import BaseModel


class HttpExceptionSchema(BaseModel):
    """
    Entidade base para as exceções HTTP genéricas ou herdadas de HTTPException da biblioteca Werkzeug.
    """

    error: str
    message: str
    status_code: int


class InternalServerErrorSchema(HttpExceptionSchema):
    """
    Entidade utilizada para apresentação de erros inesperados ocorridos na servidor.
    """


class BadRequestErrorSchema(HttpExceptionSchema):
    """
    Atributo obrigatório inválido ou não informado.
    """
