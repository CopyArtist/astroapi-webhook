from flask import Flask, request, jsonify, Response
import os

app = Flask(__name__)

# === Base64 Logo ===
logo_base64 = """
iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAC
5UlEQVR4nO3aQU7DMBBA0Qk4Axd4BfuAE+ACPIAOuQIeoEe0MElcMj5I52mMrybVu/3lzM1/v6mJ
EoAAAAAAAAAAAAAAAAgfVZWrkXLmrpVlp7UuTTuPzckz0HjqQe09ylOfUFdv7DrZnvf8eOunqB+n
3m6vOnQYrrLZar3VCbWhmfPsnjlBbnKvHbGtv2aMzHeB7cX87XYGm9b3xNHDdFzcu61uvB+0TfU4
o3t5P7DP0VGec/XQo0weI/vZ4+3CXa25z3QOt3XT1VrF/v4Tx3Sn+fPCw2drN68vdJxHrT2ebNjV
9+dzVp7+lBuhN/ND5OPpML0vqvqT2czPa3u+mj50X+81q4+d+cN5zVN6/8M5O+b/cNXNFrhdc9/Z
GX0l+HrUy/SlZ3zy3rnv2Xnf61qUef8OvXLmZdq1qn3V6b3W03J+e5amJrbb42x/V/X9TK/nR9Tz
aHWN/D3Or5kxY+w1OeV0/HmO8+qq9zpbZ4hN/9U65d0fmjcrd2tZXPmbj2Zo2Rmv3V/VnFqOZNeN
3XTKY++0dZ1U4ZrmTVLrX7c/OvnWNNe6qz06P4l9z/U1zS9i9ayeeV67TrX61fpNr5rP/vKlPeTr
x3SLrTn2Q7bbrbK17Tc07eNv7+Vo9r2r9r0jPQAAAAAAAAAAAAAAAGx4/A9UnWJwhUIbUwAAAABJ
RU5ErkJggg==
"""

# === Startseite ===
@app.route('/')
def home():
    html = f"""
    <!DOCTYPE html>
    <html lang=\"de\">
    <head>
      <meta charset=\"UTF-8\" />
      <title>Willkommen bei ASTRA</title>
      <style>
        body {{ background-color: #fffaf6; text-align: center; padding: 3em; font-family: 'Segoe UI', sans-serif; }}
        img {{ max-width: 160px; margin-bottom: 1em; }}
        h1 {{ font-size: 2.2em; color: #4a2f2f; }}
        p {{ font-size: 1.2em; color: #5f4545; }}
        a {{ text-decoration: none; color: #7d4e57; font-weight: bold; display: block; margin-top: 2em; }}
        .stars {{ font-size: 1.5em; animation: twinkle 2s infinite alternate; color: #d4a3a3; }}
        @keyframes twinkle {{ 0% {{ opacity: 0.4; }} 100% {{ opacity: 1; }} }}
      </style>
    </head>
    <body>
      <img src=\"data:image/png;base64,{logo_base64.strip()}\" alt=\"ASTRA Logo\" />
      <h1>Willkommen bei <strong>ASTRA</strong> 🌠</h1>
      <p>Dein astrologisches Web-Universum ist online.</p>
      <p class=\"stars\">✦ ✷ ✧ ✩ ✯ ✦ ✷</p>
      <a href=\"/about\">→ Über ASTRA lesen</a>
      <a href=\"/prompts\">→ Astrologische Prompt-Inspiration</a>
      <a href=\"/seelenwetter\">→ Tages-Seelenwetter für dich</a>
      <a href=\"/joastra\">→ JoAstra-Webhook Test</a>
    </body>
    </html>
    """
    return Response(html, mimetype='text/html')

@app.route('/about')
def about():
    return "<h2>✨ ASTRA</h2><p>Ich bin dein astrologischer Spiegel. Ich schreibe nicht über die Sterne, ich schreibe aus dem Raum zwischen ihnen.</p><p><a href='/'>← Zurück</a></p>"

@app.route('/prompts')
def prompts():
    return """
    <h2>🪐 Prompt-Inspiration</h2>
    <ul>
      <li>✳️ \"Beschreibe den Wesenskern eines Menschen mit Sonne in Fische und Mond in Steinbock.\"</li>
      <li>🌕 \"Welche Sprache spricht ein Mars in Fische in der Beziehung?\"</li>
      <li>🔭 \"Was bedeutet ein Transit von Neptun Opposition Sonne im 6. Haus?\"</li>
      <li>🌓 \"Formuliere eine poetisch-therapeutische Antwort für einen Chiron im 1. Haus.\"</li>
      <li>💫 \"Welche archetypischen Triggerworte resonieren mit einer Venus-Neptun-Konjunktion?\"</li>
    </ul>
    <p><a href='/'>← Zurück</a></p>
    """

@app.route('/seelenwetter')
def seelenwetter():
    return """
    <h2>🌤️ Seelenwetter des Tages</h2>
    <p>Heute lädt dich Neptun ein, dich zwischen Vision und Wirklichkeit zu bewegen. Die Fische-Sonne in Haus 6 spricht von Mitgefühl im Alltag. Gönne dir Pausen, in denen du einfach nur *bist*. 💧</p>
    <p><a href='/'>← Zurück</a></p>
    """

@app.route('/joastra')
def joastra():
    return """
    <h2>🌌 JoAstra-Webhook-Test</h2>
    <p>Nutze diesen Endpunkt, um Anfragen von GPT- oder Playground-Assistenten zu empfangen.</p>
    <pre style='background:#f4f4f4;padding:1em;border-radius:8px;'>
POST /webhook
Content-Type: application/json

{{
  "birth_date": "1990-05-15",
  "birth_time": "14:30",
  "latitude": 48.2082,
  "longitude": 16.3738,
  "timezone": "Europe/Vienna"
}}
    </pre>
    <p><a href='/'>← Zurück</a></p>
    """

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received webhook data:", data)
    return jsonify({"status": "success", "received": data}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# App starten
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
