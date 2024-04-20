import os
from flask import Flask, request, redirect, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import base64
from io import BytesIO


allowed_exts = {'jpg', 'jpeg','png','JPG','JPEG','PNG'}
app = Flask(__name__)

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

        #     img = Image.open(file.stream)
        #     img_d = img.resize((224,224))
        #     # we resize the image for the model
        #     rgbimg=None
        #     #We check if image is RGB or not
        #     if len(np.array(img_d).shape)<3:
        #         rgbimg = Image.new("RGB", img_d.size)
        #         rgbimg.paste(img_d)
        #     else:
        #         rgbimg = img_d
        #     rgbimg = np.array(rgbimg,dtype=np.float64)
        #     rgbimg = rgbimg.reshape((1,224,224,3))
        #     predictions = model.predict(rgbimg)
        #     a = int(np.argmax(predictions))
        #     if a==1:
        #         a = "pneumonic"
        #     else:
        #         a="healthy"
        # return a

        # img = Image.open(file.stream)
        return render_template('index.html', img_data=encoded_string), 200
    else:
        return render_template('index.html', img_data=""), 200

if __name__ == "__main__":
    app.debug=True
    # app.run(host='0.0.0.0')
