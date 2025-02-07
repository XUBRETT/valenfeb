from flask import Flask, render_template, send_from_directory, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient


app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

MONGO_URI = ("mongodb+srv://Valentines:12345@feb14.xrh2k.mongodb.net/?retryWrites=true&w=majority&appName=FEB14")
client = MongoClient(MONGO_URI)
db = client.db14
responses = db.dbfeb
collection = db.collection

try:
    client.server_info()  # This will throw an exception if unable to connect
    print("Successfully connected to MongoDB Atlas!")
except Exception as e:
    print("Error connecting to MongoDB Atlas:", e)
    
@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    print("Received data:", data) 
    if data and "response" in data:
        result = collection.insert_one({"response": data["response"]})
        print("Data inserted:", result.inserted_id)
        return jsonify({"message": "Response saved!"}), 200
    print("Invalid data received")
    return jsonify({"error": "Invalid data"}), 400

@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True)
