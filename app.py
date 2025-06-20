

from flask import Flask, render_template, jsonify
import json
import random

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        with open("questions.json") as f:
            questions = json.load(f)
        selected = random.sample(questions, 15)
        return render_template("index.html", questions=selected)

    @app.route("/reset")
    def reset():
        with open("questions.json") as f:
            questions = json.load(f)
        selected = random.sample(questions, 10)
        return jsonify(selected)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()











