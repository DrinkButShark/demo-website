from flask import Flask, jsonify
import os, socket

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "healthy",
        "app_name": "DevSecOps Demo Web App",
        "hostname": socket.gethostname(),
        "running_as_user": os.getenv("USER", "root"),
        "uid": os.getuid()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
