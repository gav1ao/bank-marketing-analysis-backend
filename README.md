# Bank Marketing Analysis - Backend

<div align="center">
    <img src="https://img.shields.io/badge/python-3.12%2B-yellow" alt="Python Version">
</div>

<div align="center">
  <h3 align="center">Bank Marketing Analysis</h3>
  <p align="center">
    Uma plataforma para avaliar se haverá adesão a um produto bancário.
    <br />
    <a href="https://github.com/gav1ao/bank-marketing-analysis-backend"><strong>Explore a documentação »</strong></a>
    <br />
    <br />
    <a href="https://github.com/gav1ao/bank-marketing-analysis-backend/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/gav1ao/bank-marketing-analysis-backend/issues">Solicitar Feature</a>
  </p>
</div>

---

## Sobre o Projeto

O **Bank Marketing Analysis (Backend)** é uma aplicação backend desenvolvida em Python que fornece uma REST API para 
avaliar a adesão a um produto bancário.

---

## Tecnologias Utilizadas

- [Python 3.12+](https://www.python.org/doc/)
- [Flask](https://flask.palletsprojects.com/)

---

## Como Começar

### Pré-requisitos

- Python 3.12+ instalado em sua máquina.
- `pip` (Python Package Installer) atualizado.

### Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/gav1ao/bank-marketing-analysis-backend.git
   ```

2. Navegue até o diretório do projeto:

   ```sh
   cd bank-marketing-analysis-backend
   ```

3. Crie e ative um ambiente virtual:

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

## Uso

1. Inicie a aplicação a partir de um ambiente virtual com o seguinte comando:

   ```sh
   flask run --host 0.0.0.0 --port 8080
   ```

2. A API estará disponível em: [http://localhost:8080](http://localhost:8080).

3. Consulte a documentação da API (Swagger, RapiDoc ou Redoc)para detalhes sobre os endpoints e como utilizá-los em: [http://localhost:8080/openapi/](http://localhost:8080/openapi/).

## Desenvolvimento

Durante o desenvolvimento, recomenda-se executar a aplicação utilizando o parâmetro `--reload`, pois, a cada alteração no código, o servidor será reiniciado automaticamente.

```sh
flask run --host 0.0.0.0 --port 8080 --reload
```

Execute os testes unitários através do comando

```sh
python -m pytest
```

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`).
3. Commit suas mudanças (`git commit -m 'Adiciona NovaFeature'`).
4. Faça um push para a branch (`git push origin feature/NovaFeature`).
5. Abra um Pull Request.

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## Contato

Vítor Gavião - [@vigal_jan](https://x.com/vigal_jan) - vitor.gaviao@protonmail.com

Link do Projeto: [https://github.com/gav1ao/bank-marketing-analysis-backend](https://github.com/gav1ao/bank-marketing-analysis-backend)

Link do Frontend relacionado: [https://github.com/gav1ao/bank-marketing-analysis-frontend](https://github.com/gav1ao/bank-marketing-analysis-frontend)

Link do Colab relacionado: [https://colab.research.google.com/github/gav1ao/datascience/blob/main/bank_marketing.ipynb](https://colab.research.google.com/github/gav1ao/datascience/blob/main/bank_marketing.ipynb)