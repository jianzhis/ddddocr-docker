from flask import Flask, request, jsonify
import requests
import ddddocr
import base64
import logging

app = Flask(__name__)
ocr = ddddocr.DdddOcr(beta=True)

logging.basicConfig(level=logging.INFO)

@app.route('/ocr_file', methods=['POST'])
def ocr_from_file():
    if 'file' not in request.files:
        logging.error("No file part in the request")
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        logging.error("No file selected for uploading")
        return jsonify({'error': 'No selected file'}), 400

    try:
        image_data = file.read()
        result = ocr.classification(image_data)
        return jsonify({'result': result})
    except Exception as e:
        logging.error(f"Error processing image from file: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/ocr_base64', methods=['POST'])
def ocr_from_base64():
    json_data = request.get_json()
    base64_image = json_data.get('base64_image')
    if not base64_image:
        logging.error("No base64 image provided")
        return jsonify({'error': 'No base64 image provided'}), 400

    try:
        image_data = base64.b64decode(base64_image)
        result = ocr.classification(image_data)
        return jsonify({'result': result})
    except Exception as e:
        logging.error(f"Error processing image from base64: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/ocr_url', methods=['POST'])
def ocr_from_url():
    json_data = request.get_json()
    image_url = json_data.get('image_url')
    if not image_url:
        logging.error("No image URL provided")
        return jsonify({'error': 'No image URL provided'}), 400
    
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # 确保请求成功
        image_data = response.content
        result = ocr.classification(image_data)
        return jsonify({'result': result})
    except requests.RequestException as e:
        logging.error(f"Error fetching image from URL: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
