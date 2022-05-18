import base64
import json
import re

from PIL import Image
from flask import Flask, request, jsonify, make_response
import pytesseract
import numpy as np

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify('Here we are NOW')


@app.route('/img', methods=['POST'])
def image():
    try:
        file = request.files['image']
    except Exception as err:
        print('error ocurred')
        print(err)
        return jsonify("Image not received")

    img = Image.open(file.stream)
    text = pytesseract.image_to_string(img)
    text = re.sub('[\\n,\\f]', '', text)
    osd = pytesseract.image_to_osd(img)
    osd = json.dumps(osd.replace('\n', ','))
    payload = {
        'osd': osd,
        'text': text
    }

    return make_response(payload, 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
