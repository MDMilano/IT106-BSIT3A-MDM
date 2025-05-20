from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # GET USER INPUT
        strMDMCNumber = request.form["CustomerNumber"]
        strMDMLName = request.form["LastName"]
        strMDMFName = request.form["FirstName"]
        strMDMMName = request.form["MiddleName"]
        strMDMGender = request.form["Gender"]
        strMDMBirthday = request.form["Birthday"]
        strMDMEmail = request.form["Email"]
        strMDMPSize = request.form["Size"]
        strMDMPFlavor = request.form["Flavor"]
        strMDMDrinks = request.form["Drinks"]

        if strMDMPSize == "Regular 300.00":
            sizeMDM = 300
        elif strMDMPSize == "Large 500.00":
            sizeMDM = 500
        elif strMDMPSize == "Family 800.00":
            sizeMDM = 800
        elif strMDMPSize == "Extra Large 1000.00":
            sizeMDM = 1000
        else:
            sizeMDM = 0

        if request.form.get("cheese", False):
            cheeseMDM = 50
        else:
            cheeseMDM = 0

        if request.form.get("ham", False):
            hamMDM = 60
        else:
            hamMDM = 0

        if request.form.get("bacon", False):
            baconMDM = 80
        else:
            baconMDM = 0

        if request.form.get("pepperoni", False):
            pepperoniMDM = 100
        else:
            pepperoniMDM = 0

        if strMDMPFlavor == "Hawaiian 50.00":
            flavorMDM = 50
        elif strMDMPFlavor == "Pepperoni and Cheese 100.00":
            flavorMDM = 100
        elif strMDMPFlavor == "Combination 150.00":
            flavorMDM = 150
        elif strMDMPFlavor == "Manager's Choice 200.00":
            flavorMDM = 200
        else:
            flavorMDM = 0

        if strMDMDrinks == "Softdrinks 30.00":
            drinksMDM = 30
        elif strMDMDrinks == "Mango Juice 35.00":
            drinksMDM = 35
        elif strMDMDrinks == "Pineapple Juice 40.00":
            drinksMDM = 40
        elif strMDMDrinks == "Hot Coffee 45.00":
            drinksMDM = 45
        elif strMDMDrinks == "Select One":
            drinksMDM =0
        else:
            drinksMDM = 0

        amountToPayMDM = sizeMDM + cheeseMDM + hamMDM + baconMDM + pepperoniMDM + flavorMDM + drinksMDM

        strMDMOutput = "<h3>OFFICIAL RECEIPT</h3>"
        strMDMOutput += "Customer Number: " + strMDMCNumber + "<br>"
        strMDMOutput += "Customer Name: " + strMDMLName + ", " + strMDMFName + " " + strMDMMName + "<br>"
        strMDMOutput += "Gender: " + strMDMGender + "<br>"
        strMDMOutput += "Birthday: " + strMDMBirthday + "<br>"
        strMDMOutput += "Email: " + strMDMEmail + "<br>"
        strMDMOutput += "Amount To Pay: " + str("%.1f" % amountToPayMDM) + "<br>"

        return strMDMOutput
    return render_template("mp3-mod3-it106-mdm.html")

if __name__ == "__main__":
    app.run(debug=True)
