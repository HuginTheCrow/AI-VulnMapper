
import os
import json
import openai

from flask import (
    Flask,
    render_template,
    send_from_directory,
    request, jsonify
)

from config import REPORT_DIR

app = Flask(__name__)

app.config['REPORT_FOLDER'] = str(REPORT_DIR.absolute())


@app.route('/')