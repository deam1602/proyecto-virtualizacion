import os
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv() # Carga variables del .env 

app = Flask(__name__)
CORS(app)

# Config de mongo
MONGO_USER = os.getenv("MONGO_USER", "admin")
MONGO_PASS = os.getenv("MONGO_PASS", "password")
MONGO_URL = os.getenv("MONGO_URL", f"mongodb://{MONGO_USER}:{MONGO_PASS}@mongo:27017/")
client = MongoClient(MONGO_URL)
db = client.get_database('proyecto_final')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "Backend conectado"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)