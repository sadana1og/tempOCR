import cv2
import pytesseract
import json
import glob

def ocr(path):
    img = cv2.imread(path, 0)
    custom_config = r'-l tha --psm 4'
    text = pytesseract.image_to_string(img, config=custom_config)
    return text

def process_ocr(data_path):
    with open(data_path, "r") as read_file:
        data = json.load(read_file)
    path_list = glob.glob("box_detected/out/*.png")
    idx = 0
    for path in path_list:
        img = cv2.imread(path, 0)
        custom_config = r'-l tha --psm 4'
        text = pytesseract.image_to_string(img, config=custom_config)
        data[idx]["content"] = text.replace(" ", "")
        idx += 1
    return data

if __name__ == "__main__":
    data = process_ocr("box_detected/coodinate_out.json")
    str_data = ' '.join([str(elem) for elem in data])
    encoded_unicode = str_data.encode("utf8")
    a_file = open("ocr/out/data.txt", "wb")
    a_file.write(encoded_unicode)