from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "hello docker 1.0"

from flask_script import Manager

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
