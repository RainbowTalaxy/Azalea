from flask import Flask, request, jsonify
import spacy

nlp = spacy.load("en_core_web_lg")

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello"


@app.route("/sentence", methods=["GET"])
def sentence():
    text = request.args.get("text", "")
    print(text)
    doc = nlp(text)
    return {"data": doc.to_json()}
