from flask import Flask, render_template, request
import subprocess  # For style checking

app = Flask(__name__)

# Sample route and template
@app.route("/")
def index():
    return render_template("index.html")

# Style checking function
def check_styles(css_path):
    try:
        output = subprocess.run(
            ["npm", "install", "-g", "stylelint"], capture_output=True
        )
        output = subprocess.run(
            ["stylelint", css_path], capture_output=True
        )
        if output.returncode == 0:
            return "CSS style checks passed!"
        else:
            return output.stderr.decode("utf-8")
    except FileNotFoundError:
        return "Error: 'stylelint' not installed globally. Please install using 'npm install -g stylelint'"

# Route to trigger style checks
@app.route("/check_styles")
def run_style_checks():
    result = check_styles("static/style.css")  # Replace with your CSS path
    return result

if __name__ == "__main__":
    app.run(debug=True)
