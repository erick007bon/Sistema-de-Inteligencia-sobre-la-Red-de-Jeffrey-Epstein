"""
EPSTEIN INTELLIGENCE API - LITE VERSION
Solo usa Gemini API, sin modelos locales pesados
Optimizado para Render Free Tier (512MB RAM)
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

# ============================================================
# KNOWLEDGE BASE (Embebida directo en el código)
# ============================================================
KNOWLEDGE_BASE = """
JEFFREY EPSTEIN CASE - KEY FACTS:

PEOPLE:
- Jeffrey Epstein: Financier convicted of sex trafficking. Died August 10, 2019 in Metropolitan Correctional Center, ruled suicide.
- Ghislaine Maxwell: British socialite, Epstein's associate. Convicted December 2021 on 5 of 6 counts including sex trafficking.
- Prince Andrew: Duke of York, settled civil lawsuit with Virginia Giuffre for undisclosed amount.
- Bill Clinton: Former US President, flew on Epstein's plane multiple times according to flight logs.
- Donald Trump: Former US President, had social connections with Epstein in the 1990s-2000s.
- Alan Dershowitz: Harvard Law professor, represented Epstein legally.
- Les Wexner: Billionaire, gave Epstein power of attorney and the NYC mansion.
- Jean-Luc Brunel: French modeling agent, found dead in prison February 2022.

LOCATIONS:
- Little St. James Island: Private island in US Virgin Islands, nicknamed "Pedophile Island"
- Zorro Ranch: 10,000-acre property in New Mexico
- NYC Mansion: 71st Street, largest private residence in Manhattan, gift from Wexner
- Palm Beach Estate: Florida property where initial crimes were discovered

KEY EVENTS:
- 2005: Palm Beach police begin investigation
- 2008: Epstein pleads guilty to state prostitution charges, serves 13 months
- 2019 July: Arrested on federal sex trafficking charges
- 2019 August 10: Found dead in cell
- 2021 December: Maxwell convicted
- 2024 January: Court documents unsealed revealing names of associates

DOCUMENTS:
- Flight logs showing passengers on "Lolita Express" (Boeing 727)
- Black book with contacts
- Court depositions from victims
- FBI investigation files
"""

# ============================================================
# GEMINI CLIENT (Lightweight)
# ============================================================
def get_gemini_response(question: str) -> str:
    """Get response from Gemini API"""
    try:
        from google import genai
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return "❌ Error: GOOGLE_API_KEY not configured"
        
        client = genai.Client(api_key=api_key)
        
        prompt = f"""You are an intelligence analyst expert on the Jeffrey Epstein case.
Answer the following question using ONLY the information provided below.
Be concise but informative. If the information is not in the context, say so.

CONTEXT:
{KNOWLEDGE_BASE}

QUESTION: {question}

ANSWER:"""
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        
        return response.text
        
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ============================================================
# FLASK APP
# ============================================================
def create_api():
    app = Flask(__name__)
    CORS(app)
    
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "status": "online",
            "service": "Epstein Intelligence API (Lite)",
            "version": "2.0",
            "endpoints": ["/api/health", "/api/chat"]
        })
    
    @app.route("/api/health", methods=["GET"])
    def health():
        return jsonify({
            "status": "healthy",
            "gemini": bool(os.getenv("GOOGLE_API_KEY")),
            "mode": "lite"
        })
    
    @app.route("/api/chat", methods=["POST"])
    def chat():
        try:
            data = request.get_json()
            question = data.get("question", "")
            
            if not question:
                return jsonify({"error": "No question provided"}), 400
            
            answer = get_gemini_response(question)
            
            return jsonify({
                "answer": answer,
                "sources": ["DOJ Documents", "Court Records", "Flight Logs"],
                "mode": "gemini-lite"
            })
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    return app

# Entry point
app = create_api()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    print(f"🚀 Starting Epstein Intelligence API (Lite) on port {port}")
    app.run(host="0.0.0.0", port=port)
