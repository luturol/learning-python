import os
from flask import Flask, jsonify

app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'title': 'Read the Flask Mega Tutorial',
        'description': 'This tutorial will teach you how to code a Rest API using Flask in Python',
        'done': False
    },
    {
        'id': 2,
        'title': 'Code an App using Flask in Python',
        'description': 'Create an Rest API using Flask and post on Github',
        'done': False
    }
]

@app.route("/")
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)