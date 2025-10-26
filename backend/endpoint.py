from flask import Flask, request, jsonify
import tempfile
import os
from pathlib import Path

# Import the helper that talks to Gemini
from backend.Gemini import get_gemini_response

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    """Accepts a multipart/form-data POST with optional 'prompt' and optional file 'image'.

    Returns JSON: {"result": <text response from Gemini>}.
    """
    # prompt can come in form-data or JSON body
    prompt = request.form.get("prompt")
    if not prompt:
        json_body = request.get_json(silent=True) or {}
        prompt = json_body.get("prompt")

    image = request.files.get("image")
    tmp_path = None
    try:
        if image:
            # Save uploaded image to a temp file and pass the path to Gemini helper
            suffix = Path(image.filename).suffix or ".jpg"
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
            image.save(tmp.name)
            tmp_path = tmp.name

        # Require at least a prompt or an image
        if not prompt and not tmp_path:
            return jsonify({"error": "Please provide a 'prompt' or upload an 'image'."}), 400

        # Call the Gemini helper
        result = get_gemini_response(prompt or "", image_path=tmp_path)
        return jsonify({"result": result})
    finally:
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass


if __name__ == "__main__":
    # For local testing only. In production run with a proper WSGI server.
    app.run(host="0.0.0.0", port=8000, debug=True)
