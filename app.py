from flask import Flask, render_template, request, jsonify
from src.detector import detect_sensitivity  #detector.py
from datetime import datetime

app = Flask(__name__)

# Route to load the chat interface
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    message = data['message']
    
    is_sensitive = detect_sensitivity(message)
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] Message received: {message}")
    
    response = {
        'sensitive': is_sensitive,
        'sensitive_message': "This message contains sensitive information." if is_sensitive else ""
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
