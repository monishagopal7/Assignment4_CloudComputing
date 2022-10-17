
from flask import Flask,render_template,jsonify
import requests
import json
import random
import os

app = Flask(__name__)

@app.route('/',methods= ['GET'])
def index():
    res = requests.get('http://api:5000/api/pickrandom')
    menu_item = res.text
    return render_template('menu.html', menu=menu_item)

# @app.route('/api/pickrandom',methods= ['GET'])
# def randres():
#     res = key, val = random.choice(list(menu.items()))
#     return (str(res))

if __name__ == "__main__":
       app.run(debug=True, host='0.0.0.0', port=80)
    # port = int(os.environ.get('PORT', 3001))
    # app.run('127.0.0.1', port = port,debug=True)
 
