from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/routes')
def get_routes():
    with open('sample_routes.json') as f:
        routes = json.load(f)
    return jsonify(routes)

if __name__ == '__main__':
    app.run(debug=True)
