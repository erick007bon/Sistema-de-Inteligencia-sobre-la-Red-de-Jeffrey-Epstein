"""WSGI entry point for production"""
from src.ai_backend import create_api

app = create_api()

if __name__ == "__main__":
    app.run()
