# API de Análisis de Sentimientos 🎭

API que analiza el sentimiento de textos en español, clasificándolos como positivos, negativos o neutrales.

## 🛠 Tecnologías usadas
- FastAPI
- TextBlob
- Python 3.9+
- Uvicorn

## 📝 Funcionalidad

La API tiene un endpoint principal:

### POST /analizar
Envías:
```json
{
  "texto": "Me encanta esta API!"
}

Recibes:
{
  "texto": "Me encanta esta API!",
  "sentimiento": "positivo",
  "confianza": 0.85
}

👤 Autor

Camilo Vega 