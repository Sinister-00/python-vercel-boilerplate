from flask import Flask,render_template,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'status': 'success', 'message': 'server is running 🚀'})

if __name__ == '__main__':
    app.run(debug=True)