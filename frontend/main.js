document.addEventListener("DOMContentLoaded", function () {
    const runButton = document.getElementById("runButton");
    const languageSelector = document.getElementById("language");
    const codeEditor = document.getElementById("codeEditor");
    const outputBox = document.getElementById("output");

    if (!runButton || !languageSelector || !codeEditor || !outputBox) {
        console.error("One or more elements are missing. Check your HTML IDs.");
        return;
    }

    runButton.addEventListener("click", async function () {
        const language = languageSelector.value;
        const code = codeEditor.value;

        if (!language || !code) {
            outputBox.innerText = "❌ Error: Missing language or code.";
            return;
        }

        try {
            outputBox.innerText = "⏳ Running..."; // Show loading message

            const response = await fetch("http://127.0.0.1:5000/execute", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ language, code }),
            });

            const result = await response.json();
            console.log("Server Response:", result); // Debugging log

            outputBox.innerText = result.output || result.error || "❌ Error: No output received.";
        } catch (error) {
            outputBox.innerText = "❌ Failed to connect to the server.";
            console.error(error);
        }
    });
});
