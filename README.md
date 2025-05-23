# Comparación de Rendimiento: Groq Cloud vs Fal AI

Este proyecto realiza una comparación de rendimiento entre dos proveedores de IA: Groq Cloud y Fal AI, utilizando el modelo Llama 4 Maverick en ambos casos.

## 🚀 Características

- Comparación de tiempos de respuesta entre Groq Cloud y Fal AI
- Uso del mismo modelo (Llama 4 Maverick) para una comparación justa
- Análisis detallado de rendimiento con métricas de porcentaje y factor multiplicativo
- Configuración simple mediante variables de entorno

## 📋 Prerrequisitos

- Python 3.8 o superior
- Cuenta en Groq Cloud con API key
- Cuenta en Fal AI con API key

## 🔧 Instalación

1. Clona el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd groqcloud-test
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura las variables de entorno:
   - Crea un archivo `.env` en la raíz del proyecto
   - Agrega tus API keys:
```env
GROQ_API_KEY=tu_clave_api_de_groq
FAL_KEY=tu_clave_api_de_fal
```

## 🎯 Uso

Ejecuta el script principal:
```bash
python main.py
```

El script realizará las siguientes acciones:
1. Enviará el mismo prompt a ambos servicios
2. Medirá los tiempos de respuesta
3. Mostrará una comparación detallada del rendimiento

## 📊 Resultados

El script mostrará:
- Tiempo de respuesta de Groq Cloud
- Tiempo de respuesta de Fal AI
- Comparación en porcentaje
- Factor multiplicativo de la diferencia

## 🔍 Detalles Técnicos

- **Modelo utilizado**: Llama 4 Maverick
- **Parámetros**:
  - Temperature: 0.7
  - Max tokens: 2048
- **Prompt**: Problema matemático complejo para evaluar el rendimiento

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios que te gustaría hacer.

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📧 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue en el repositorio.

---
Desarrollado con ❤️ para la comunidad de IA