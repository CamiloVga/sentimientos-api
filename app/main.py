from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

# Inicializar FastAPI
app = FastAPI(title="API de Sentimientos")

# Definir estructura de datos
class TextoInput(BaseModel):
    texto: str

@app.get("/")
def read_root():
    return {"mensaje": "¡Bienvenido a la API de Análisis de Sentimientos!"}

@app.post("/analizar")
def analizar_sentimiento(texto_input: TextoInput):
    # Crear TextBlob object
    analysis = TextBlob(texto_input.texto)
    
    # Obtener polaridad (-1 a 1)
    polaridad = analysis.sentiment.polarity
    
    # Determinar sentimiento
    if polaridad <= -0.1:
        sentimiento = "negativo"
    elif polaridad >= 0.1:
        sentimiento = "positivo"
    else:
        sentimiento = "neutral"
        
    return {
        "texto": texto_input.texto,
        "sentimiento": sentimiento,
        "confianza": round((polaridad + 1) / 2, 2)  # Convertir a escala 0-1
    }