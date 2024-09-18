from flask import Flask, request
from markupsafe import escape
from flask import render_template 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html')

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port=8000, debug=True)
    
