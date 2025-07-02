# Webhook Server para Kushki (Flask)

Este microservicio recibe webhooks de Kushki y expone endpoints para consultar el estado y la devolución.

## Endpoints
- POST `/webhook` — Recibe el webhook de Kushki
- GET `/get-estado` — Devuelve el último estado de pago recibido
- GET `/get-devolucion` — Devuelve la última devolución recibida

## Deploy en Render
- Build command: `pip install -r requirements.txt`
- Start command: `python webhook_server.py`
- El puerto se configura automáticamente con la variable de entorno `PORT`. 