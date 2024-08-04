from flask import Flask, request, Response
import os, json, re

app = Flask(__name__)

@app.route("/register_user", methods=['POST'])
def register():
    if request.method == 'POST':
        return None, 200
    return None, 404