import prediction
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/predictor')
def predictor():
   return render_template("predictor.html")

@app.route('/prediction', methods=["GET", "POST"])
def predict():
    
    if request.method == "GET":
        return "Kindly Fill The Form First & Then Click On The Predict Button To Get The Prediction !"

    if request.method == "POST":

        empid = request.form.get("empid")
        satisfaction = request.form.get("satisfaction")
        evaluation = request.form.get("evaluation")
        project = request.form.get("projects")
        hours = request.form.get("hours")
        time = request.form.get("years")
        accident = request.form.get("accident")
        promotion = request.form.get("promotion")
        department = request.form.get("department")
        sal = request.form.get("salary")

        results=prediction.predict(satisfaction,evaluation,project,hours,time,accident,promotion,department,sal)

        if(results):
            a="Prediction - The Employee Will Leave The Company."
        else:
            a="Prediction - The Employee Will Not Leave The Company."

        if(int(accident)):
            accident_str="Yes"
        else:
            accident_str="No"

        if(int(promotion)):
            promotion_str="Yes"
        else:
            promotion_str="No"

        if(department=="accounting"): department_str="Accounting"
        if(department=="hr"): department_str="HR"
        if(department=="IT"): department_str="IT"
        if(department=="management"): department_str="Management"
        if(department=="product_mng"): department_str="Product Management"
        if(department=="RandD"): department_str="R & D"
        if(department=="sales"): department_str="Sales"
        if(department=="support"): department_str="Support"
        if(department=="technical"): department_str="Technical"
        
        if(sal=="low"): sal_str="Low"
        if(sal=="medium"): sal_str="Medium"
        if(sal=="high"): sal_str="High"
        
        return render_template("prediction.html",x=results,y=a,a1=satisfaction,a2=evaluation,a3=project,a4=hours,a5=time,a6=accident_str,a7=promotion_str,a8=department_str,a9=sal_str,a10=empid)

if __name__ == "__main__":
    app.run(debug=True)