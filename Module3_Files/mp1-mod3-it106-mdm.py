from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # GET USER INPUT
        strMDMID = request.form["PatientID"]
        strMDMLName = request.form["LastName"]
        strMDMFName = request.form["FirstName"]
        strMDMAge = request.form["Age"]
        strMDMRType = request.form["RoomType"]
        strMDMRPDay = request.form["RatePerDay"]
        strMDMNODays = request.form["NoOfDays"]
        strMDMLCharges = request.form["LaboratoryCharges"]
        strMDMECharges = request.form["ExtraCharges"]

        def w():
            strMDMRDescription = "Ward"
            return strMDMRDescription

        def spr():
            strMDMRDescription = "Semi Private Room"
            return strMDMRDescription

        def pr():
            strMDMRDescription = "Private Room"
            return strMDMRDescription

        def er():
            strMDMRDescription = "Executive or Suite Room"
            return strMDMRDescription

        def icu():
            strMDMRDescription = "Intensive Care Unit"
            return strMDMRDescription

        def nicu():
            strMDMRDescription = "Neonatal Intensive Care Unit"
            return strMDMRDescription

        def picu():
            strMDMRDescription = "Pediatric Intensive Care Unit"
            return strMDMRDescription

        def ic():
            strMDMRDescription = "Incubator Cost"
            return strMDMRDescription

        switcher = {
            "W": w,
            "SPR": spr,
            "PR": pr,
            "ER": er,
            "ICU": icu,
            "NICU": nicu,
            "PICU": picu,
            "IC": ic
        }

        def getSwitch(argument):
            # Get the function from the switcher dictionary
            func = switcher.get(argument, lambda: "No Room Type")
            return func()

        strMDMRDesc = getSwitch(strMDMRType)

        strMDMAGName = ""
        Age = int(strMDMAge)
        if Age >= 0 and Age <=2:
            strMDMAGName = "Babies"
        elif Age >= 3 and Age <=16:
            strMDMAGName = "Children"
        elif Age >= 17 and Age <=30:
            strMDMAGName = "Young Adults"
        elif Age >= 31 and Age <=45:
            strMDMAGName = "Middle Aged Adults"
        elif Age > 45:
            strMDMAGName = "Old Adults"
        else:
            strMDMAGName = "Invalid Age"

        RoomCharge  = float(strMDMRPDay) * float(strMDMNODays)
        TotalAmount = RoomCharge + float(strMDMLCharges) + float(strMDMECharges)
        HealthInsurance = TotalAmount * 0.05
        PhilHealth = TotalAmount * 0.06
        SSS = TotalAmount * 0.07
        TotalDiscount = HealthInsurance + PhilHealth + SSS
        AmountToPay = TotalAmount - TotalDiscount

        strMDMOutput = "<h3>OFFICIAL RECEIPT</h3>"
        strMDMOutput += "Patient ID: " + strMDMID + "<br>"
        strMDMOutput += "Patient Name: " + strMDMLName + ", " + strMDMFName + "<br>"
        strMDMOutput += "Age: " + str(strMDMAge) + "<br>"
        strMDMOutput += "Age Group Name: " + strMDMAGName + "<br>"
        strMDMOutput += "Room Type: " + strMDMRType + "<br>"
        strMDMOutput += "Room Description: " + strMDMRDesc + "<br>"
        strMDMOutput += "Rate Per Day: " + str(strMDMRPDay) + "<br>"
        strMDMOutput += "No. of Days: " + str(strMDMNODays) + "<br>"
        strMDMOutput += "Laboratory Charges: " + str(strMDMLCharges) + "<br>"
        strMDMOutput += "Extra Charges: " + str(strMDMECharges) + "<br>"
        strMDMOutput += "Room Charge: " + str("%.2f" % RoomCharge) + "<br>"
        strMDMOutput += "Total Amount: " + str("%.2f" % TotalAmount) + "<br>"
        strMDMOutput += "Health Insurance: " + str("%.2f" % HealthInsurance) + "<br>"
        strMDMOutput += "PhilHealth: " + str("%.2f" % PhilHealth) + "<br>"
        strMDMOutput += "SSS: " + str("%.2f" % SSS) + "<br>"
        strMDMOutput += "Total Discount: " + str("%.2f" % TotalDiscount) + "<br>"
        strMDMOutput += "Amount To Pay: " + str("%.2f" % AmountToPay) + "<br>"

        return strMDMOutput
    return render_template("mp1-mod3-it106-mdm.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)