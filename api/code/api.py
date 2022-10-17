from flask import Flask,render_template,jsonify
import json
import random

app = Flask(__name__)
 
menu = {"Dum Biryani" : 15, "Peanut Butter Jam Toast": 4, "Dose Chuntey" :16, "Wheat Beer":12,"Pilsner":7 , "Coffee":7 , "German Beer":4 , "Butter Chicken": 17.5,
"Spice Vegan Wonton":16.6, "Sesame Noodles":18 , "Mushroom Manchurian": 13 , "Love" : 100000000000000000, "Life" :9908447474774 , "Hope" : 8383387637637, "Vodka" : 923874927}

@app.route('/')
def homepage():
    s = "Hello my lovely humans and robots!!!!!!"
    return render_template('index.html', text = s)

@app.route("/api/menu",methods = ['GET'])
def menu_item():
    return jsonify({"menu":menu})

@app.route('/api/pickrandom',methods= ['GET'])
def randres():

       key1 = random.choice(list(menu))
       return str(key1) + ':' + str(menu[key1])


if __name__ == "__main__":
     app.run('0.0.0.0', port=5000,debug=True)
    

