from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/') # http://www.mysite.com/
def home():
    return jsonify({'message': True})

if __name__ == '__main__':
    app.run()