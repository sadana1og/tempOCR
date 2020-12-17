#text_detection.py
import cv2
import requests

def call_text_detection_api(img_path, url):
    files = {'file': open(img_path, 'rb')}
    r = requests.post(url, files=files)
    with open("text_detected/out/text_detected_img.png", 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    return r
    
if __name__ == "__main__":
    url = 'http://localhost:8080/detect?debugger=true'
    call_text_detection_api("input/doc_627_0_0.jpg", url)