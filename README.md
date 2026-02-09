# 🕵️ Epstein Intelligence System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Next.js](https://img.shields.io/badge/Next.js-16-black?logo=next.js)
![Flask](https://img.shields.io/badge/Flask-3.1-green?logo=flask)
![Gemini](https://img.shields.io/badge/Gemini-2.0-purple?logo=google)
![Render](https://img.shields.io/badge/Render-Deployed-success?logo=render)
![Vercel](https://img.shields.io/badge/Vercel-Live-black?logo=vercel)

**Sistema de Inteligencia Artificial para Análisis Forense de Documentos**

[🌐 Demo en Vivo](https://webapp-ten-cyan.vercel.app) • [📡 API Endpoint](https://sistema-de-inteligencia-sobre-la-red-de.onrender.com) • [📄 Documentación](#arquitectura)

</div>

---

## 📋 Descripción

Sistema de **Inteligencia Artificial** diseñado para el análisis forense de documentos judiciales utilizando técnicas avanzadas de **NLP (Procesamiento de Lenguaje Natural)** y **RAG (Retrieval-Augmented Generation)**.

El proyecto procesa y analiza documentos del caso Epstein liberados por el Departamento de Justicia de EE.UU., extrayendo entidades, relaciones y patrones mediante algoritmos de Machine Learning.

---

## 🏗️ Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND (Vercel)                         │
│   Next.js 16 + TypeScript + Tailwind CSS + D3.js Force Graph    │
│                  webapp-ten-cyan.vercel.app                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼ HTTPS API Calls
┌─────────────────────────────────────────────────────────────────┐
│                        BACKEND (Render)                          │
│         Python Flask + Gemini 2.0 Flash + REST API              │
│      sistema-de-inteligencia-sobre-la-red-de.onrender.com       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      AI/ML LAYER                                 │
│  • Gemini 2.0 Flash (LLM)      • NLP Entity Extraction          │
│  • Sentence-BERT (Embeddings)   • Sentiment Analysis            │
│  • RAG Pipeline                 • Anomaly Detection             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA LAYER                                  │
│  • 14,000+ documentos procesados                                │
│  • 500+ entidades extraídas (personas, organizaciones, lugares) │
│  • Grafos de conexiones con PageRank                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Tecnologías Utilizadas

### Backend (Python)
| Tecnología | Uso |
|------------|-----|
| **Flask 3.1** | Framework API REST |
| **Gunicorn** | WSGI HTTP Server (Producción) |
| **Google Gemini 2.0 Flash** | Large Language Model para RAG |
| **Sentence-BERT** | Embeddings semánticos |
| **spaCy** | NLP - Extracción de entidades |
| **CORS** | Cross-Origin Resource Sharing |

### Frontend (TypeScript)
| Tecnología | Uso |
|------------|-----|
| **Next.js 16** | React Framework (SSR/SSG) |
| **TypeScript** | Tipado estático |
| **Tailwind CSS** | Estilos utility-first |
| **D3.js Force Graph** | Visualización de redes |
| **Leaflet** | Mapas interactivos |
| **Recharts** | Gráficos y estadísticas |

### Infraestructura
| Servicio | Rol |
|----------|-----|
| **Render** | Backend hosting (API REST) |
| **Vercel** | Frontend hosting (CDN global) |
| **GitHub** | Control de versiones + CI/CD |

---

## 🧠 Funcionalidades de IA

### 1. Chat con RAG (Retrieval-Augmented Generation)
```python
# El sistema responde preguntas basándose en documentos reales
POST /api/chat
{
    "question": "Who is Ghislaine Maxwell?"
}
```

### 2. Extracción de Entidades (NER)
- **Personas**: 127 individuos identificados
- **Organizaciones**: 45 entidades corporativas
- **Ubicaciones**: 38 lugares georeferenciados
- **Fechas**: 200+ referencias temporales
- **Dinero**: Transacciones financieras detectadas

### 3. Análisis de Sentimiento
- Clasificación: Positivo / Negativo / Neutral
- Score de riesgo por documento
- Detección de anomalías

### 4. Visualización de Grafos
- Red de conexiones entre personas
- Algoritmo PageRank para importancia
- Clustering de comunidades

---

## 📡 API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/` | Status del servidor |
| `GET` | `/api/health` | Health check |
| `POST` | `/api/chat` | Chat con IA (RAG) |

### Ejemplo de Uso

```bash
# Health Check
curl https://sistema-de-inteligencia-sobre-la-red-de.onrender.com/api/health

# Chat con IA
curl -X POST https://sistema-de-inteligencia-sobre-la-red-de.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What happened on August 10, 2019?"}'
```

---

## 🖥️ Instalación Local

### Requisitos
- Python 3.11+
- Node.js 18+
- API Key de Google Gemini

### Backend
```bash
cd PROYECTOS/07_document_forensics
pip install -r requirements.txt
echo "GOOGLE_API_KEY=tu_api_key" > .env
python src/ai_backend.py
```

### Frontend
```bash
cd webapp
npm install
npm run dev
```

---

## 📊 Resultados del Análisis

| Métrica | Valor |
|---------|-------|
| Documentos procesados | 14,000+ |
| Entidades extraídas | 500+ |
| Personas identificadas | 127 |
| Ubicaciones mapeadas | 38 |
| Referencias de dinero | 45 |
| Conexiones en grafo | 156 |
| Anomalías detectadas | 5 |

---

## 🌐 Demo en Producción

| Componente | URL |
|------------|-----|
| **Web App** | https://webapp-ten-cyan.vercel.app |
| **API REST** | https://sistema-de-inteligencia-sobre-la-red-de.onrender.com |

---

## 📁 Estructura del Proyecto

```
07_document_forensics/
├── src/
│   └── ai_backend.py          # Backend completo con RAG
├── app.py                     # Entry point para Render
├── webapp/
│   ├── src/
│   │   ├── app/
│   │   │   └── page.tsx       # Página principal
│   │   └── components/
│   │       ├── AIChat.tsx     # Chat con IA
│   │       ├── NetworkGraph.tsx # Grafo de conexiones
│   │       ├── SearchPanel.tsx  # Búsqueda de documentos
│   │       └── MapAndAnomalies.tsx # Mapa + Anomalías
│   └── public/
│       └── data/              # Datos procesados (JSON)
├── data/
│   └── processed/             # Entidades y análisis
├── requirements.txt           # Dependencias Python
└── README.md                  # Este archivo
```

---

## 👤 Autor

**Erick Reinaldo Flores Zambrano**

- 🎓 Estudiante de Ingeniería en Datos e Inteligencia Artificial
- 🏛️ Universidad Técnica de Manabí (UTM)
- 📍 Machala, El Oro, Ecuador 🇪🇨
- 🔗 [GitHub](https://github.com/erick007bon)
- 💼 [LinkedIn](https://linkedin.com/in/erick-flores-zambrano)

---

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE) para más detalles.

---

## ⚠️ Disclaimer

Este proyecto es únicamente para **fines educativos y de investigación**. Los datos provienen de documentos públicos liberados por el Departamento de Justicia de EE.UU. y están disponibles en [HuggingFace Datasets](https://huggingface.co/datasets).

---

<div align="center">

**⭐ Si te gustó este proyecto, dale una estrella en GitHub ⭐**

</div>
