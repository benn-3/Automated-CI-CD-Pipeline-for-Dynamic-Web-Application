from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Returns a styled HTML page."""
    target = os.environ.get('TARGET', 'World')
    
    # --- Start of HTML & CSS ---
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My CI/CD Project</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f2f5;
            }}
            .container {{
                text-align: center;
                padding: 40px;
                background-color: #ffffff;
                border-radius: 12px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            }}
            .logo {{
                font-size: 48px;
                font-weight: bold;
                color: #0d6efd; /* A nice blue color */
            }}
            h1 {{
                font-size: 28px;
                color: #333;
                margin-top: 10px;
            }}
            p {{
                font-size: 18px;
                color: #555;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">App</div>
            <h1>Hello, {target}!</h1>
            <p>This app is deployed by our automated CI/CD pipeline.</p>
        </div>
    </body>
    </html>
    """
    # --- End of HTML & CSS ---
    
    return html_content

if __name__ == "__main__":
    # The app will run on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

