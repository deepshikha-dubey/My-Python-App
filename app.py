from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    current_time = datetime.datetime.now()

    return f"""
    <html>
    <head>
        <title>My DevOps App</title>
        <style>
            body {{
                font-family: Arial;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                color: white;
                text-align: center;
                padding-top: 100px;
            }}
            .box {{
                background: rgba(0,0,0,0.3);
                padding: 30px;
                border-radius: 10px;
                display: inline-block;
            }}
            h1 {{
                color: #ffeb3b;
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 Thanks Universe for everything!</h1>
            <h2>My DevOps Project is Running 🎉</h2>
            <p><b>Container Hostname:</b> {hostname}</p>
            <p><b>Current Time:</b> {current_time}</p>
            <p>🐳 Running inside Docker</p>
        </div>
    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)