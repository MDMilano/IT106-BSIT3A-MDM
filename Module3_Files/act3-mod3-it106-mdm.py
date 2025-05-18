from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # GET USER INPUT
        strMDMID = request.form["CustomerID"]
        strMDMName = request.form["CustomerName"]

        # GET SELECT RADIOBUTTON
        strMDMOrder = request.form["order"]
        if strMDMOrder == "Hamburger":
            ordersMDM = 50
        elif strMDMOrder == "Cheese Burger":
            ordersMDM = 100
        elif strMDMOrder == "Big MacJabee":
            ordersMDM = 150

        # GET SELECTED CHECKBOXES
        if request.form.get("patty", False):
            pattyMDM = 25
        else:
            pattyMDM = 0

        if request.form.get("coles", False):
            colesMDM = 50
        else:
            colesMDM = 0

        if request.form.get("hamegg", False):
            hameggMDM = 100
        else:
            hameggMDM = 0

        # GET SELECTED DRINKS
        strMDMDrinks = request.form["drinks"]
        if strMDMDrinks == "SOFTDRINKS 30.00":
            drinksMDM = 30
        elif strMDMDrinks == "COFFEE 40.00":
            drinksMDM = 40
        elif strMDMDrinks == "MANGO JUICE 50.00":
            drinksMDM = 50

        totalMDM = ordersMDM + pattyMDM + colesMDM + hameggMDM + drinksMDM

        strMDMOutput = "<h3>OFFICIAL RECEIPT</h3>"
        strMDMOutput += "Customer ID: " + strMDMID + "<br>"
        strMDMOutput += "Customer Name: " + strMDMName + "<br>"
        strMDMOutput += "Total Amount: " + str(totalMDM) + "<br>"

        return strMDMOutput
    return render_template("act3-mod3-it106-mdm.html")

if __name__ == "__main__":
    app.run()
