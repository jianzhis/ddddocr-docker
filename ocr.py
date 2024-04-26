from flask import Flask, request, jsonify
import os
import requests
from datetime import datetime
import ddddocr
import base64

app = Flask(__name__)
ocr = ddddocr.DdddOcr(beta=True)

# 确保 images 文件夹存在
os.makedirs('images', exist_ok=True)

@app.route('/ocr_url', methods=['POST'])
def ocr_from_url():
    json_data = request.get_json()
    image_url = json_data.get('image_url')
    if not image_url:
        return jsonify({'error': 'No image URL provided'}), 400
    
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # 确保请求成功
        image_data = response.content
        return process_image(image_data)
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/ocr_base64', methods=['POST'])
def ocr_from_base64():
    json_data = request.get_json()
    base64_image = json_data.get('base64_image')
    if not base64_image:
        return jsonify({'error': 'No base64 image provided'}), 400

    try:
        image_data = base64.b64decode(base64_image)
        return process_image(image_data)
    except Exception as e:
        return jsonify({'error': 'Invalid base64 data'}), 400

def process_image(image_data):
    try:
        # 构造文件名并保存图片
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
        image_path = os.path.join('images', f'image_{timestamp}.png')
        with open(image_path, 'wb') as f:
            f.write(image_data)

        # 使用 ddddocr 进行识别
        with open(image_path, 'rb') as f:
            result = ocr.classification(f.read())

        # 删除文件
        os.remove(image_path)

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # 确保即使在出现异常时也删除文件
        if os.path.exists(image_path):
            os.remove(image_path)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
