"""Entry point for Render deployment"""
from src.ai_backend import create_api

app = create_api()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
