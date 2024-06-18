import requests
from config import TOKEN, AGENT_ID, BASE_URL

def send_message(message):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }

    data = {
        "agent_id": AGENT_ID,
        "input": message,
        "enableStreaming": False,
    }

    response = requests.post(f"{BASE_URL}/agents/{AGENT_ID}/invoke", headers=headers, json=data)
    print("Received response from superagent", response.json())

