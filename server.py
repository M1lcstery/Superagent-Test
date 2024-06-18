from flask import Flask, request, jsonify
from pyngrok import ngrok, conf
from message_processing import send_message

app = Flask(__name__)
NGROK_URL = None  # Initialize as None to indicate it's not yet set

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        print("GET")
        VERIFY_TOKEN = "12345"  # Reemplaza con tu token real
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == VERIFY_TOKEN:
            return challenge
        else:
            return "Invalid verification token", 403

    if request.method == 'POST':
        data = request.get_json()

        if 'messages' in data['entry'][0]['changes'][0]['value']:
            # Handle incoming message events (e.g., send a reply)
            message = data['entry'][0]['changes'][0]['value']['messages'][0]
            print(f"Received message: {message}")

            text = message["text"]["body"]
            send_message(text)
            
        if 'statuses' in data['entry'][0]['changes'][0]['value']:
            # Handle message status events (e.g., read, delivered)
            status = data['entry'][0]['changes'][0]['value']['statuses'][0]
            print(f"Message status update: {status}")


    return jsonify({'success': True}), 200


def run_ngrok():
    global NGROK_URL 
    conf.get_default().config_path = "ngrok.yml"
    tunnel = ngrok.connect(name="whatsapp")
    NGROK_URL = tunnel.public_url
    print(f"Public URL: {NGROK_URL}")
    print(tunnel)

def create_app():  # Function to create and return the Flask app
    # ... (your webhook and other routes)s

    return app

# Removed the direct call to app.run() from this module
