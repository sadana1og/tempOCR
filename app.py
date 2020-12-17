#app.py

from flask import Flask, render_template, request, redirect, url_for
from text_detection import call_text_detection_api
from box_detection import box_extraction
from ocr import process_ocr

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

@app.route('/ocr', methods=['POST'])
def upload_file():
    uploaded_file = request.files['img']
    if uploaded_file.filename != '':
        uploaded_file.save("input/in_image.png")
        img_w_boundingbox = call_text_detection_api(img_path="input/in_image.png",
                                                    url='http://localhost:8080/detect?debugger=true')
        box_extraction("text_detected/out/text_detected_img.png", "input/in_image.png" , "./box_detected/out/")
        data = process_ocr("box_detected/coodinate_out.json")
        str_data = ' '.join([str(elem) for elem in data])
        encoded_unicode = str_data.encode("utf8")
        a_file = open("ocr/out/data.txt", "wb")
        a_file.write(encoded_unicode)
    return encoded_unicode