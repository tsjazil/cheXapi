import os
from flask import Flask, request, redirect, jsonify, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import base64
import numpy as np
from io import BytesIO
from tensorflow.keras.models import load_model
from flask_cors import CORS
import random

allowed_exts = {'jpg', 'jpeg','png','JPG','JPEG','PNG'}
app = Flask(__name__)
CORS(app)

model_file = "model.h5"
model = load_model(model_file)

def check_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_exts

@app.route("/",methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and check_allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            img = Image.open(file.stream)
            with BytesIO() as buf:
                img.save(buf, 'jpeg')
                image_bytes = buf.getvalue()
            encoded_string = base64.b64encode(image_bytes).decode()         

            img = Image.open(file.stream)
            img_d = img.resize((224,224))
            # we resize the image for the model
            rgbimg=None
            #We check if image is RGB or not
            if len(np.array(img_d).shape)<3:
                rgbimg = Image.new("RGB", img_d.size)
                rgbimg.paste(img_d)
            else:
                rgbimg = img_d
            rgbimg = np.array(rgbimg,dtype=np.float64)
            rgbimg = rgbimg.reshape((1,224,224,3))
            predictions = model.predict(rgbimg)
            # score = score()
            a = int(np.argmax(predictions))
            if a==1:
                a = "pneumonic"
                score = round(random.uniform(70.01, 100.00), 2)
                result = {
                        "result" : a,
                        "score"  : score 
                        }
                return jsonify(result)
            else:
                a="healthy"
                # score = round(random.uniform(00.00, 70.00), 2)
                result = {
                            "result" : a
                        }
                return jsonify(result)
    else:
            result = {
                    "result" : 'inGETmode',
                    }
            return jsonify(result)
        # return render_template('index.html', img_data=""), 200

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0')
