from flask import Flask
app = Flask(__name__)

@app.route('/') # http://www.mysite.com/
def home():
    return {'message': True}

if __name__ == '__main__':
    app.run()