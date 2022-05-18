import base64

from PIL import Image
from flask import Flask, request, jsonify
import io
import numpy as np

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Here we are'


@app.route('/img', methods=['POST'])
def image():
    try:
        file = request.files['image']
    except Exception as err:
        print('error ocurred')
        print(err)
        return "Image not received"
    img = Image.open(file.stream)
    img.save('received-img.png')
    dataB64 = base64.b64encode(file.stream.read())
    image_np = np.array(dataB64)
    return jsonify({
        'size': [img.width, img.height],
        'format': img.format,
        'img': dataB64
    })


if __name__ == '__main__':
    app.run(debug=True)
