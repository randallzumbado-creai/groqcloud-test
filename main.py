import time
import fal_client
import os
from dotenv import load_dotenv
from groq import Groq

# Cargar variables de entorno
load_dotenv()

# Configuración de clientes
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
fal_client.api_key = os.getenv("FAL_KEY")

# Prompt complejo para la prueba
PROMPT = """Analiza y resuelve el siguiente problema matemático complejo paso a paso:

Dado un sistema de ecuaciones diferenciales:
dx/dt = 2x + y
dy/dt = -x + 3y

Con condiciones iniciales x(0) = 1, y(0) = 2

1. Encuentra los valores propios de la matriz de coeficientes
2. Determina los vectores propios correspondientes
3. Escribe la solución general del sistema
4. Aplica las condiciones iniciales para encontrar la solución particular
5. Verifica que la solución satisface el sistema original

Explica cada paso detalladamente y muestra todos los cálculos intermedios."""

def test_groq():
    start_time = time.time()
    
    completion = groq_client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[
            {"role": "system", "content": "Eres un experto en matemáticas y análisis de sistemas."},
            {"role": "user", "content": PROMPT}
        ],
        temperature=0.7,
        max_tokens=2048
    )
    
    end_time = time.time()
    return end_time - start_time, completion.choices[0].message.content

def test_fal():
    start_time = time.time()
    
    handle = fal_client.submit(
        "fal-ai/any-llm",
        arguments={
            "model": "meta-llama/llama-4-maverick",
            "prompt": PROMPT,
            "temperature": 0.7,
            "max_tokens": 2048
        }
    )
    
    # Esperar y obtener la respuesta
    response = handle.get()
    end_time = time.time()
    
    # La respuesta es directamente el texto
    content = str(response)
    
    return end_time - start_time, content

def main():
    print("Iniciando prueba de velocidad...\n")
    
    # Prueba Groq
    print("Probando Groq Cloud...")
    groq_time, _ = test_groq()
    print(f"Tiempo de respuesta Groq: {groq_time:.2f} segundos\n")
    
    # Prueba Fal
    print("Probando Fal AI...")
    fal_time, _ = test_fal()
    print(f"Tiempo de respuesta Fal: {fal_time:.2f} segundos\n")
    
    # Comparación
    print("=== Resultados ===")
    print(f"Groq Cloud: {groq_time:.2f} segundos")
    print(f"Fal AI: {fal_time:.2f} segundos")
    
    if groq_time < fal_time:
        diferencia_porcentaje = ((fal_time - groq_time) / groq_time) * 100
        factor = fal_time / groq_time
        print(f"\nGroq Cloud fue {diferencia_porcentaje:.1f}% más rápido que Fal AI")
        print(f"Groq Cloud fue {factor:.1f}x más rápido que Fal AI")
    else:
        diferencia_porcentaje = ((groq_time - fal_time) / fal_time) * 100
        factor = groq_time / fal_time
        print(f"\nFal AI fue {diferencia_porcentaje:.1f}% más rápido que Groq Cloud")
        print(f"Fal AI fue {factor:.1f}x más rápido que Groq Cloud")

if __name__ == "__main__":
    main() 