import subprocess
import os
import uuid

def run_javascript(code):
    filename = f"script_{uuid.uuid4().hex}.js"

    try:
        with open(filename, "w") as f:
            f.write(code)

        process = subprocess.run(
            ["node", filename],
            capture_output=True,
            text=True,
            timeout=5
        )

        return {
            "output": process.stdout.strip(),
            "error": process.stderr.strip() if process.returncode != 0 else ""
        }
    except subprocess.TimeoutExpired:
        return {"error": "Execution timed out"}
    finally:
        os.remove(filename)
