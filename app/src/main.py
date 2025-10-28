from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Returns a styled HTML page."""
    target = os.environ.get('TARGET', 'World')
    
    # --- Start of HTML & CSS ---
    # We'll use Tailwind CSS for a modern, aesthetic design
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My CI/CD Project</title>
        
        <!-- Load Tailwind CSS -->
        <script src="https://cdn.tailwindcss.com"></script>
        
        <!-- Load Inter font (a clean, modern font) -->
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet">
        
        <!-- Configure Tailwind to use Inter -->
        <script>
          tailwind.config = {{
            theme: {{
              extend: {{
                fontFamily: {{
                  sans: ['Inter', 'sans-serif'],
                }},
              }}
            }}
          }}
        </script>
        
        <style>
            /* A small custom style for a gradient text effect */
            .gradient-text {{
                background-image: linear-gradient(to right, #4f46e5, #a855f7); /* Indigo to Purple */
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
            }}
        </style>
    </head>
    
    <!-- 
      - font-sans: Applies the Inter font
      - bg-gray-50: A very light gray background
      - flex, items-center, justify-center, min-h-screen: Vertically and horizontally centers the content
    -->
    <body class="font-sans bg-gray-50 flex items-center justify-center min-h-screen p-4">
    
        <!-- 
          - container: (Not a Tailwind class, but descriptive)
          - mx-auto: Horizontal margin auto (for centering)
          - max-w-md: Limits the maximum width on large screens
          - w-full: Takes full width on small screens
          - p-8: Adds generous padding
          - bg-white: White background for the card
          - rounded-2xl: Large rounded corners
          - shadow-xl: A prominent, soft shadow
          - border, border-gray-100: A very subtle border
          - text-center: Centers all text
        -->
        <div class="container mx-auto max-w-md w-full p-8 bg-white rounded-2xl shadow-xl border border-gray-100 text-center">
            
            <!-- Logo area with gradient text -->
            <div class="text-6xl font-black gradient-text">
                App
            </div>
            
            <!-- Main heading -->
            <h1 class="text-4xl font-bold text-gray-800 mt-6">
                Hello, {target}!
            </h1>
            
            <!-- Subtitle -->
            <p class="text-lg text-gray-600 mt-3">
                This app is deployed by our automated CI/CD pipeline.
            </p>

            <!-- 
              A little extra flair that fits the CI/CD theme
              - mt-8, pt-6: Adds spacing above
              - border-t, border-gray-200: Adds a top border line
            -->
            <div class="mt-8 pt-6 border-t border-gray-200">
                <p class="text-sm text-gray-400">
                    CI/CD Status: <span class="font-semibold text-green-500">All systems operational</span>
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    # --- End of HTML & CSS ---
    
    return html_content

if __name__ == "__main__":
    # The app will run on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
