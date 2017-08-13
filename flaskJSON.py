from flask import Flask
app = Flask(__name__)

import json
import random


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dice')
def dice():
    dice = {
        'dice1': random.randint(1, 6),
        'dice2': random.randint(1, 6)
    }
    return json.dumps(dice)

if __name__ == '__main__':
    app.debug = True
    app.run()
