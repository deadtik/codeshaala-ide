from flask import Flask, request, jsonify
import os
from compilers.cpp_runner import run_cpp
from compilers.java_runner import run_java
from compilers.js_runner import run_javascript
from compilers.python_runner import run_python

app = Flask(__name__)

# Language mapping to functions
language_runners = {
    "cpp": run_cpp,
    "java": run_java,
    "javascript": run_javascript,
    "python": run_python
}

@app.route("/execute", methods=["POST"])
def execute_code():
    data = request.get_json()
    
    language = data.get("language")
    code = data.get("code")
    user_input = data.get("user_input", "")

    if not language or not code:
        return jsonify({"error": "Missing required fields"}), 400

    if language not in language_runners:
        return jsonify({"error": "Unsupported language"}), 400

    result = language_runners[language](code, user_input)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
