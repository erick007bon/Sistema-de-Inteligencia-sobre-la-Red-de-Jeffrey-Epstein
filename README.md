# 🕵️ Sistema de Inteligencia sobre la Red de Jeffrey Epstein

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Machine Learning](https://img.shields.io/badge/ML-Sentence--BERT-green)
![Deep Learning](https://img.shields.io/badge/DL-Gemini%202.0-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📊 Descripción

Sistema de **Inteligencia Artificial** que analiza más de **11,000 documentos** del Departamento de Justicia de Estados Unidos (DOJ) relacionados con el caso Jeffrey Epstein.

### 🧠 Tecnologías de IA Utilizadas

| Componente | Tecnología | Tipo |
|------------|------------|------|
| **Chat RAG** | Google Gemini 2.0 Flash | Deep Learning |
| **Búsqueda Semántica** | Sentence-BERT (all-MiniLM-L6-v2) | Machine Learning |
| **NER** | spaCy | Machine Learning |
| **Embeddings** | Sentence Transformers | Deep Learning |
| **Backend** | Flask + Gunicorn | Python |

## 🚀 Características

- ✅ **RAG (Retrieval-Augmented Generation)**: Respuestas basadas en documentos reales
- ✅ **Búsqueda Semántica**: Busca por significado, no solo palabras clave
- ✅ **API REST**: Endpoints para integrar con cualquier frontend
- ✅ **Base de Conocimiento**: 20+ documentos clave indexados

## 📡 API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/health` | Estado del sistema |
| POST | `/api/chat` | Chat con RAG + Gemini |
| POST | `/api/search` | Búsqueda semántica |

### Ejemplo de uso:

```bash
# Health check
curl http://localhost:5001/api/health

# Chat con RAG
curl -X POST http://localhost:5001/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "Who is Ghislaine Maxwell?"}'

# Búsqueda semántica
curl -X POST http://localhost:5001/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "flights to island", "top_k": 5}'
```

## 🛠️ Instalación Local

```bash
# Clonar repositorio
git clone https://github.com/erick007bon/Sistema-de-Inteligencia-sobre-la-Red-de-Jeffrey-Epstein.git
cd Sistema-de-Inteligencia-sobre-la-Red-de-Jeffrey-Epstein

# Instalar dependencias
pip install -r requirements.txt

# Configurar API key de Gemini
echo "GOOGLE_API_KEY=tu_api_key_aqui" > .env

# Ejecutar
python src/ai_backend.py
```

## 🌐 Deploy a Railway (Gratis)

1. Fork este repositorio
2. Ve a [railway.app](https://railway.app)
3. Conecta tu cuenta de GitHub
4. Selecciona este repositorio
5. Agrega la variable `GOOGLE_API_KEY` en Settings > Variables
6. ¡Listo! Railway despliega automáticamente

## 📊 Datos Analizados

| Métrica | Cantidad |
|---------|----------|
| Documentos DOJ | 8,429 |
| Text Messages | 3,377 |
| Total | **11,806** |
| Personas identificadas | 562 |
| Organizaciones | 1,381 |
| Ubicaciones | 425 |

## 👤 Autor

**Erick Reinaldo Flores Zambrano**
- 🔗 GitHub: [@erick007bon](https://github.com/erick007bon)
- 🇪🇨 Ecuador

## 📄 Licencia

MIT License - Uso libre con atribución.

---

⭐ Si te gusta este proyecto, dale una estrella en GitHub!
