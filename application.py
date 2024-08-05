from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

