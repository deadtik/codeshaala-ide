import subprocess
import os

def run_java(code):
    filename = "Main.java"

    try:
        # Write Java code to file
        with open(filename, "w") as f:
            f.write(code)

        # Compile Java file
        compile_process = subprocess.run(
            ["javac", filename], capture_output=True, text=True
        )

        # Check if compilation failed
        if compile_process.returncode != 0:
            return {"error": "Compilation failed", "details": compile_process.stderr}

        # Run the compiled Java class
        run_process = subprocess.run(
            ["java", "-cp", ".", "Main"], capture_output=True, text=True, timeout=5
        )

        # Check if execution failed
        if run_process.returncode != 0:
            return {"error": "Runtime Error", "details": run_process.stderr}

        return {"output": run_process.stdout}

    except subprocess.TimeoutExpired:
        return {"error": "Execution timed out"}

    finally:
        # Clean up files safely
        if os.path.exists(filename):
            os.remove(filename)
        if os.path.exists("Main.class"):
            os.remove("Main.class")
