from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
import uuid
from compilers.python_runner import run_python
from compilers.cpp_runner import run_cpp
from compilers.java_runner import run_java
from compilers.js_runner import run_javascript

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Language execution mapping
language_executors = {
    "python": run_python,
    "cpp": run_cpp,
    "java": run_java,
    "javascript": run_javascript
}

@app.route("/execute", methods=["POST"])
def execute_code():
    data = request.get_json()
    
    language = data.get("language")
    code = data.get("code", "")
    user_input = data.get("input", "")

    if not language or not code:
        return jsonify({"error": "Missing language or code"}), 400

    executor = language_executors.get(language.lower())

    if not executor:
        return jsonify({"error": f"Unsupported language: {language}"}), 400

    try:
        result = executor(code, user_input)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
