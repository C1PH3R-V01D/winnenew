from flask import Flask,request,render_template
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/predict",methods=['POST','GET'])
def survival():
    fixed_acidity=float(request.form.get("fixed_acidity"))	
    volatile_acidity=float(request.form.get("volatile_acidity"))	
    citric_acid=float(request.form.get("citric_acid"))
    chlorides=float(request.form.get("chlorides"))	
    total_sulfur_dioxide=float(request.form.get("total_sulfur_dioxide"))	
    density=float(request.form.get("density"))
    sulphates=float(request.form.get("sulphates"))	
    alcohol=float(request.form.get("alcohol"))

    result=model.predict(np.array([fixed_acidity,volatile_acidity,citric_acid,chlorides,total_sulfur_dioxide,density,sulphates,alcohol]).reshape(1,8))
    if result[0]==1:
        return "<h1 style='color:green'>Good Quality Of Wine</h1>"
    else:
        return "<h1 style='color:red'>Good Quality Of Wine</h1>"
app.run(host="0.0.0.0",port=8080)