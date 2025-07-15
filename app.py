from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

client = MongoClient(os.getenv("MONGO_URI"))
try:
    client.admin.command('ping')
    print("Connected to MongoDB")
except Exception as e:
    print("MongoDB connection is failed",e)    
db = client.webhooks
collection = db.events

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Webhook endpoint was hit!")
    data = request.json
    print("Payload",data)
    event_type = request.headers.get('X-GitHub-Event')
    print("Github events",event_type)
    processed = parse_event(data, event_type)
    if processed:
        print("Parsed events",processed)
        collection.insert_one(processed)
    return jsonify({"status": "received"}), 200

@app.route('/events', methods=['GET'])
def get_events():
    docs = list(collection.find().sort("timestamp", -1).limit(10))
    for doc in docs:
        doc['_id'] = str(doc['_id'])
    return jsonify(docs)

def parse_event(payload, event_type):
    try:
        if event_type == "push":
            return {
                "event": "push",
                "author": payload["pusher"]["name"],
                "to_branch": payload["ref"].split("/")[-1],
                "timestamp": datetime.utcnow()
            }
        elif event_type == "pull_request":
            return {
                "event": "pull_request",
                "author": payload["pull_request"]["user"]["login"],
                "from_branch": payload["pull_request"]["head"]["ref"],
                "to_branch": payload["pull_request"]["base"]["ref"],
                "timestamp": datetime.utcnow()
            }
        elif event_type == "merge":
            # Optional: GitHub sends merge events inside pull_request with merged:true
            pass
        return None
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == '__main__':
    app.run(debug=True)
    
    
    