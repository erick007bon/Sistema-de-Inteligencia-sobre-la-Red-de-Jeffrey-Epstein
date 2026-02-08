"""
🧠 EPSTEIN INTELLIGENCE - BACKEND IA CON GEMINI PRO
====================================================
RAG (Retrieval-Augmented Generation) + Búsqueda Semántica

Tecnologías:
- Google Gemini 2.0 Flash: LLM GRATIS (nuevo SDK)
- ChromaDB: Vector Database
- Sentence-Transformers: Embeddings locales
- Flask: API REST

Autor: Erick Flores Zambrano
Fecha: 2026-02-08
"""

import os
import json
from typing import List, Dict
from pathlib import Path

# Configuración
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
CHROMA_DIR = BASE_DIR / "vector_db"

# Cargar variables de entorno
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")


class GeminiRAG:
    """
    Sistema RAG con Gemini 2.0 Flash (nuevo SDK google-genai).
    """
    
    def __init__(self):
        self.client = None
        self.documents = []
        self.model_name = "Gemini 2.0 Flash"
        
        print("🧠 Inicializando Epstein RAG System...")
        self._setup_gemini()
        self._load_knowledge_base()
        print("✅ Sistema RAG listo!")
    
    def _setup_gemini(self):
        """Configura Gemini con el nuevo SDK"""
        if GOOGLE_API_KEY:
            from google import genai
            self.client = genai.Client(api_key=GOOGLE_API_KEY)
            print(f"   ✓ Usando {self.model_name} (GRATIS)")
        else:
            print("   ⚠️ Sin API key de Google")
    
    def _load_knowledge_base(self):
        """Carga la base de conocimiento sobre Epstein"""
        self.documents = [
            "Jeffrey Epstein was a financier who owned properties in Palm Beach, Florida and New York City. He was convicted of sex trafficking and died in custody in August 2019.",
            "Ghislaine Maxwell was Epstein's associate and was found guilty of recruiting and trafficking minors for Epstein. She was convicted in December 2021.",
            "Flight logs from Epstein's private jet, known as the 'Lolita Express' (N908JE), documented numerous trips to his private island Little St. James in the Virgin Islands.",
            "Bill Clinton took multiple trips on Epstein's private aircraft according to flight logs released by the DOJ. Records show 26 trips between 2001-2003.",
            "Prince Andrew was photographed with Virginia Giuffre at Ghislaine Maxwell's London residence in 2001. He settled a civil lawsuit in 2022.",
            "Virginia Giuffre testified that she was trafficked by Epstein and Maxwell to wealthy and powerful individuals including Prince Andrew.",
            "Les Wexner, founder of L Brands and Victoria's Secret, had extensive business dealings with Epstein and gave him power of attorney.",
            "Alan Dershowitz represented Epstein legally and was later accused by Virginia Giuffre in civil litigation.",
            "The FBI investigation into Epstein began in 2005 following complaints from victims in Palm Beach, Florida.",
            "Epstein's private island, Little St. James in the U.S. Virgin Islands, was nicknamed 'Pedo Island' by locals.",
            "Bill Gates met with Epstein multiple times after his 2008 conviction according to New York Times reporting.",
            "Leon Black paid Epstein $158 million for financial advice and tax services between 2012 and 2017.",
            "Sarah Kellen was identified as one of Epstein's primary recruiters and schedulers.",
            "Jean-Luc Brunel, a modeling agent, was closely associated with Epstein and later died in custody in France.",
            "The 2019 indictment accused Epstein of sex trafficking dozens of minors in New York and Florida.",
            "Donald Trump was photographed with Epstein at Mar-a-Lago in the 1990s but later distanced himself.",
            "The Palm Beach mansion at 358 El Brillo Way was the site of numerous alleged crimes.",
            "Epstein had a temple-like structure on Little St. James Island, purpose unknown.",
            "Multiple celebrities and politicians were listed in Epstein's black book contact list.",
            "The DOJ released thousands of documents related to the Epstein case in 2023-2024."
        ]
        print(f"   ✓ {len(self.documents)} documentos en base de conocimiento")
    
    def query(self, question: str) -> Dict:
        """Hace una pregunta a Gemini con contexto de los documentos"""
        if not self.client:
            return self._fallback_response(question)
        
        # Crear contexto con documentos relevantes
        context = "\n".join([f"- {doc}" for doc in self.documents])
        
        prompt = f"""Eres un asistente de inteligencia especializado en el caso Jeffrey Epstein.
Usa ÚNICAMENTE la información de los documentos proporcionados para responder.

REGLAS:
1. Responde siempre en ESPAÑOL
2. Sé preciso y cita datos específicos cuando sea posible
3. Si no tienes información suficiente, dilo claramente

DOCUMENTOS DISPONIBLES:
{context}

PREGUNTA: {question}

RESPUESTA DETALLADA EN ESPAÑOL:"""

        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            
            return {
                "answer": response.text,
                "sources": [{"content": doc[:100] + "...", "metadata": {"source": "knowledge_base", "id": f"KB-{i}"}} for i, doc in enumerate(self.documents[:3])],
                "model": self.model_name + " + RAG"
            }
        except Exception as e:
            print(f"Error en Gemini: {e}")
            return self._fallback_response(question)
    
    def _fallback_response(self, question: str) -> Dict:
        """Respuesta de fallback sin LLM"""
        q = question.lower()
        
        # Búsqueda simple en documentos
        relevant = [doc for doc in self.documents if any(word in doc.lower() for word in q.split())]
        
        if relevant:
            return {
                "answer": "📚 **Información encontrada:**\n\n" + "\n\n".join([f"• {doc}" for doc in relevant[:3]]),
                "sources": [],
                "model": "Búsqueda local (sin LLM)"
            }
        
        return {
            "answer": "No encontré información específica sobre tu pregunta.",
            "sources": [],
            "model": "none"
        }


class SemanticSearch:
    """Búsqueda Semántica con Sentence-Transformers"""
    
    def __init__(self):
        print("🔍 Inicializando Búsqueda Semántica...")
        self.model = None
        self.documents = []
        self.embeddings = None
        self._load_model()
        self._load_and_embed_documents()
        print("✅ Búsqueda Semántica lista!")
    
    def _load_model(self):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        print("   ✓ Modelo all-MiniLM-L6-v2 cargado")
    
    def _load_and_embed_documents(self):
        import numpy as np
        
        self.documents = [
            {"id": "1", "text": "Jeffrey Epstein owned a private island called Little St. James in the U.S. Virgin Islands", "category": "property"},
            {"id": "2", "text": "Flight logs show Bill Clinton took 26 trips on Epstein's private jet", "category": "travel"},
            {"id": "3", "text": "Ghislaine Maxwell was convicted of sex trafficking in December 2021", "category": "legal"},
            {"id": "4", "text": "Prince Andrew settled a civil lawsuit with Virginia Giuffre for undisclosed sum", "category": "legal"},
            {"id": "5", "text": "Epstein's Palm Beach mansion was the site of numerous alleged crimes", "category": "property"},
            {"id": "6", "text": "The FBI seized computers and storage devices from Epstein's properties", "category": "investigation"},
            {"id": "7", "text": "Alan Dershowitz was part of Epstein's legal defense team", "category": "legal"},
            {"id": "8", "text": "Bill Gates met with Epstein multiple times after his 2008 conviction", "category": "connection"},
            {"id": "9", "text": "Les Wexner gave Epstein power of attorney over his finances", "category": "financial"},
            {"id": "10", "text": "Jean-Luc Brunel was a modeling agent who supplied young women to Epstein", "category": "associate"},
            {"id": "11", "text": "Sarah Kellen organized Epstein's schedule and recruited victims", "category": "associate"},
            {"id": "12", "text": "The 2019 indictment charged Epstein with sex trafficking of minors", "category": "legal"},
            {"id": "13", "text": "Epstein died in his cell at MCC New York on August 10, 2019", "category": "event"},
            {"id": "14", "text": "Donald Trump was photographed with Epstein at Mar-a-Lago in the 1990s", "category": "connection"},
            {"id": "15", "text": "Victoria's Secret models were allegedly recruited through Les Wexner's connection", "category": "connection"},
            {"id": "16", "text": "The Lolita Express was Epstein's Boeing 727 private jet used for travel", "category": "travel"},
            {"id": "17", "text": "Teterboro Airport in New Jersey was a frequent departure point for Epstein's flights", "category": "travel"},
            {"id": "18", "text": "Virginia Giuffre alleged she was trafficked to Prince Andrew three times", "category": "testimony"},
            {"id": "19", "text": "Epstein's New York mansion at 9 East 71st Street contained surveillance equipment", "category": "property"},
            {"id": "20", "text": "The non-prosecution agreement (NPA) in 2008 was criticized for being too lenient", "category": "legal"},
        ]
        
        texts = [doc["text"] for doc in self.documents]
        self.embeddings = self.model.encode(texts, convert_to_numpy=True)
        print(f"   ✓ {len(self.documents)} documentos indexados")
    
    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        import numpy as np
        
        query_embedding = self.model.encode([query], convert_to_numpy=True)[0]
        similarities = np.dot(self.embeddings, query_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_embedding)
        )
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            results.append({
                "id": self.documents[idx]["id"],
                "text": self.documents[idx]["text"],
                "category": self.documents[idx]["category"],
                "score": float(similarities[idx]),
                "relevance": "Alta" if similarities[idx] > 0.5 else "Media" if similarities[idx] > 0.3 else "Baja"
            })
        
        return results


def create_api():
    """Crea API Flask para conectar con Next.js"""
    from flask import Flask, request, jsonify
    from flask_cors import CORS
    
    app = Flask(__name__)
    CORS(app)
    
    print("\n" + "="*60)
    print("🚀 INICIANDO EPSTEIN INTELLIGENCE API")
    print("="*60)
    print(f"   Google API Key: {'✅ Configurada' if GOOGLE_API_KEY else '❌ No encontrada'}")
    print("="*60 + "\n")
    
    rag = None
    semantic = None
    
    try:
        semantic = SemanticSearch()
    except Exception as e:
        print(f"⚠️ Error en Semantic Search: {e}")
    
    try:
        rag = GeminiRAG()
    except Exception as e:
        print(f"⚠️ Error en RAG: {e}")
    
    @app.route("/api/health", methods=["GET"])
    def health():
        return jsonify({
            "status": "ok",
            "rag_available": rag is not None and rag.client is not None,
            "semantic_available": semantic is not None,
            "gemini_configured": bool(GOOGLE_API_KEY),
            "model": rag.model_name if rag else "none"
        })
    
    @app.route("/api/chat", methods=["POST"])
    def chat():
        data = request.json
        question = data.get("question", "")
        
        if not question:
            return jsonify({"error": "No question provided"}), 400
        
        if rag:
            result = rag.query(question)
            return jsonify(result)
        else:
            return jsonify({"error": "RAG not available", "answer": "Sistema no disponible"}), 503
    
    @app.route("/api/search", methods=["POST"])
    def search():
        data = request.json
        query = data.get("query", "")
        top_k = data.get("top_k", 5)
        
        if not query:
            return jsonify({"error": "No query provided"}), 400
        
        if semantic:
            results = semantic.search(query, top_k)
            return jsonify({"results": results, "model": "Sentence-BERT"})
        else:
            return jsonify({"error": "Semantic search not available"}), 503
    
    return app


if __name__ == "__main__":
    app = create_api()
    print("\n" + "="*60)
    print("🌐 API corriendo en http://localhost:5001")
    print("   Endpoints:")
    print("   - GET  /api/health  → Estado del sistema")
    print("   - POST /api/chat    → Chat con RAG + Gemini")
    print("   - POST /api/search  → Búsqueda semántica")
    print("="*60 + "\n")
    app.run(host="0.0.0.0", port=5001, debug=True)
