from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html", spr = "Karkoli")
    #return "<p>Hello, World!</p>"


@app.route("/calcLove", methods= ["POST"])
def calcLove():
    tmp = dict(request.form)
    ime1 = tmp.get("ime1")
    ime2 = tmp.get("ime2")
    r = f"{ime1} + {ime2} = {random.randint(0,100)} %"
    
    if len(ime1)==0 or len(ime2)==0:
        r = f"{ime1} + {ime2} = {random.randint(0,0)} %"
    
    if ime1=="tia" or ime2=="tia":
        r=f"{ime1} + {ime2} = {random.randint(90,100)} %"
    
    if ime1=="nika" or ime2=="nika":
        r=f"{ime1} + {ime2} = {random.randint(0,5)} %"

    return render_template("index.html", rezultat = r)
    #return f"{ime1} + {ime2} = {random.randint(0,100)} %"
    


app.run(debug= True)