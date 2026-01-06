from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ku">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sblood - Color Picker</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #ffffff;
            color: #000000;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        header {
            text-align: center;
            padding: 40px 20px;
        }

        header h1 {
            font-size: 48px;
            font-weight: bold;
            color: #000000;
        }

        main {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 30px;
            padding: 20px;
        }

        .color-picker-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }

        #colorPicker {
            width: 200px;
            height: 200px;
            border: 3px solid #000000;
            border-radius: 10px;
            cursor: pointer;
        }

        #colorDisplay {
            width: 250px;
            height: 100px;
            border: 3px solid #000000;
            border-radius: 10px;
            background-color: #ff0000;
        }

        .code-display {
            background-color: #f5f5f5;
            padding: 20px 40px;
            border-radius: 10px;
            border: 2px solid #000000;
        }

        #colorCode {
            font-family: 'Courier New', monospace;
            font-size: 24px;
            color: #000000;
            font-weight: bold;
        }

        footer {
            padding: 30px;
            text-align: center;
        }

        .telegram-link {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            color: #000000;
            transition: transform 0.3s ease;
        }

        .telegram-link:hover {
            transform: scale(1.1);
        }

        .telegram-link svg {
            color: #0088cc;
        }

        .telegram-text {
            font-size: 20px;
            font-weight: bold;
            color: #ff0000;
        }
    </style>
</head>
<body>
    <header>
        <h1>Sblood</h1>
    </header>

    <main>
        <div class="color-picker-container">
            <input type="color" id="colorPicker" value="#ff0000">
            <div id="colorDisplay"></div>
        </div>

        <div class="code-display">
            <p id="colorCode">color: #ff0000;</p>
        </div>
    </main>

    <footer>
        <a href="https://t.me/Shblood" target="_blank" class="telegram-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69.01-.03.01-.14-.07-.2-.08-.06-.19-.04-.27-.02-.12.02-1.96 1.25-5.54 3.67-.52.36-.99.53-1.42.52-.47-.01-1.37-.26-2.03-.48-.82-.27-1.47-.42-1.42-.88.03-.24.37-.49 1.02-.75 4-1.74 6.68-2.88 8.03-3.43 3.82-1.59 4.61-1.87 5.13-1.87.11 0 .37.03.53.16.14.11.18.26.2.37.01.08.03.29.01.45z"/>
            </svg>
            <span class="telegram-text">Shblood</span>
        </a>
    </footer>

    <script>
        const colorPicker = document.getElementById('colorPicker');
        const colorDisplay = document.getElementById('colorDisplay');
        const colorCode = document.getElementById('colorCode');

        colorPicker.addEventListener('input', function() {
            const selectedColor = this.value;
            colorDisplay.style.backgroundColor = selectedColor;
            colorCode.textContent = `color: ${selectedColor};`;
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)