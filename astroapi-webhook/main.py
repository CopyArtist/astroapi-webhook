from flask import Flask, request, jsonify, Response
import os
import base64

app = Flask(__name__)

# Willkommen auf /
@app.route('/')
def home():
    # Eingebettetes Logo als Base64 (aus Platzgründen gekürzt)
    logo_base64 = """
    iVBORw0KGgoAAAANSUhEUgAAAJYAAACWCAYAAADLPAySAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB...
    """
    html = f"""
    <!DOCTYPE html>
    <html lang="de">
    <head>
      <meta charset="UTF-8" />
      <title>Willkommen bei ASTRA</title>
      <style>
        body {{ background-color: #fffaf6; text-align: center; padding: 3em; font-family: 'Segoe UI', sans-serif; }}
        img {{ max-width: 180px; margin-bottom: 1.5em; }}
        h1 {{ font-size: 2em; color: #4a2f2f; }}
        p {{ font-size: 1.2em; color: #5f4545; }}
      </style>
    </head>
    <body>
      <img src="data:image/png;base64,{logo_base64.strip()}" alt="ASTRA Logo" />
      <h1>Willkommen bei ASTRA 🌠</h1>
      <p>Dein astrologisches Web-Universum ist online.</p>
    </body>
    </html>
    """
    return Response(html, mimetype='text/html')

# Webhook auf /webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received webhook data:", data)
    return jsonify({"status": "success", "received": data}), 200

# App starten
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
