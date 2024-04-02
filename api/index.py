from flask import Flask,render_template,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'status': 'success', 'message': 'server is running 🚀'})

@app.route('/render')
def about():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)