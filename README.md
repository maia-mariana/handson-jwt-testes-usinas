# Handson: JWT e Testes Unitários no CRUD de Usinas

Projeto Ciência de Dados II — Bulbe Energia.

API de Usinas em FastAPI (arquitetura em 4 camadas) com:

- **Autenticação JWT**: `POST`, `PUT` e `DELETE` em `/v1/usinas` exigem token. Consultas (`GET`) continuam públicas.
- **Testes automatizados com pytest**: Domínio, segurança (hash e JWT), Services e API via `TestClient` — 28 testes.

## Como rodar

```bash
python -m venv venv
venv\Scripts\activate          # Windows  (Linux/Mac: source venv/bin/activate)
pip install -r requirements.txt
uvicorn app.main:app --reload  # Swagger em http://localhost:8000/docs
pytest -v                      # 28 passed
```

## Rotas

| Rota | Acesso |
|---|---|
| `POST /v1/auth/registrar` | público |
| `POST /v1/auth/login` (formulário `username` + `password`) | público |
| `GET /v1/auth/me` | token |
| `GET /v1/usinas`, `GET /v1/usinas/{id}` | público |
| `POST /v1/usinas`, `PUT /v1/usinas/{id}`, `DELETE /v1/usinas/{id}` | token |

Sem token, com token falso ou expirado (30 min), a resposta é `401`:

```json
{"error": {"code": "TOKEN_INVALIDO", "message": "Token ausente, invalido ou expirado.", "status": 401}}
```
