
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "食選轉盤後端API運行中"

@app.route('/process_menu', methods=['POST'])
def process_menu():
    data = request.json
    return jsonify({
        "status": "success",
        "message": "菜單已處理",
        "recognized_items": data.get("items", [])
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
