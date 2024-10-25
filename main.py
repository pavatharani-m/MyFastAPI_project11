from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    # Serve the combined HTML, CSS, and JavaScript in one file
    content = """
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sentiment Analysis Tool</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #4B0082;
        }
        textarea {
            width: 100%;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        button {
            width: 100%;
            padding: 15px;
            background-color: #9370DB; /* Lavender */
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #6a5acd; /* Dark Slate Blue */
        }
        #result {
            padding: 15px;
            background-color: #f0f8ff;
            border: 1px solid #ccc;
            margin-top: 10px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .filter-buttons {
            margin-top: 20px;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }
        .reset-button {
            background-color: #ffc107;
        }
        .reset-button:hover {
            background-color: #e0a800;
        }
        .download-button {
            background-color: #17a2b8;
        }
        .download-button:hover {
            background-color: #138496;
        }
        .emotion {
            font-size: 24px;
            text-align: center;
            margin-top: 20px;
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sentiment Analysis Tool</h1>
        <form id="sentiment-form">
            <textarea id="input-text" rows="10" placeholder="Enter text here..."></textarea>
            <button type="submit">Analyze Sentiment</button>
        </form>
        <h2>Result</h2>
        <div id="result"></div>
    </div>
    <div class="container">
        <h1>Image Upload and Filter Application</h1>

        <label for="upload">Choose an Image</label>
        <input type="file" id="upload" accept="image/*" />

        <canvas id="canvas"></canvas>

        <div class="filter-buttons">
            <button onclick="applyFilter('grayscale')" disabled id="grayscaleBtn">Grayscale</button>
            <button onclick="applyFilter('sepia')" disabled id="sepiaBtn">Sepia</button>
            <button onclick="applyFilter('brightness')" disabled id="brightnessBtn">Brightness</button>
        </div>

        <div class="filter-buttons">
            <button onclick="resetImage()" disabled id="resetBtn" class="reset-button">Reset</button>
            <button onclick="downloadImage()" disabled id="downloadBtn" class="download-button">Download</button>
        </div>
    </div>
    <div class="container">
        <h1>Emotion Recognition Studio</h1>
        <button id="startRecording">🎤 Start Recording</button>
        <button id="stopRecording" disabled>🛑 Stop Recording</button>
        <div class="emotion" id="emotionDisplay">
            <span id="emotion">Neutral</span>
        </div>
    </div>
    <script>
        // JavaScript for handling functionalities
        document.getElementById('sentiment-form').addEventListener('submit', async function(event) {
            event.preventDefault();
            const inputText = document.getElementById('input-text').value;
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams({ text: inputText })
            });
            const data = await response.json();
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = `<strong>Sentiment:</strong> ${data.sentiment} <br> <strong>Confidence:</strong> ${data.confidence}%`;
        });
        // Additional JavaScript code goes here
    </script>
</body>
</html>
    """
    return HTMLResponse(content=content)