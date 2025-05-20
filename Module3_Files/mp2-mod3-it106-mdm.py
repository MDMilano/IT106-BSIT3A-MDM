from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # GET USER INPUT
        strMDMSNumber = request.form["StudentNumber"]
        strMDMLName = request.form["LastName"]
        strMDMFName = request.form["FirstName"]
        strMDMMName = request.form["MiddleName"]
        strMDMGender = request.form["gender"]
        strMDMEmail = request.form["Email"]
        strMDMCourse = request.form["Course"]
        strMDMTuition = request.form["Tuition"]
        strMDMScholar = request.form["ScholarShips"]

        if strMDMTuition == "1st Year":
            tuitionMDM = 500
        elif strMDMTuition == "2nd Year":
            tuitionMDM = 600
        elif strMDMTuition == "3rd Year":
            tuitionMDM = 800
        elif strMDMTuition == "4th Year":
            tuitionMDM = 900
        else:
            tuitionMDM = 0

        if request.form.get("regfee", False):
            regfeeMDM = 100
        else:
            regfeeMDM = 0

        if request.form.get("intfee", False):
            intfeeMDM = 100
        else:
            intfeeMDM = 0

        if request.form.get("idfee", False):
            idfeeMDM = 100
        else:
            idfeeMDM = 0

        if request.form.get("libfee", False):
            libfeeMDM = 50
        else:
            libfeeMDM = 0

        if strMDMScholar == "DEAN'S LISTER 200.00":
            scholarMDM = 200
        elif strMDMScholar == "STUDENT ASSISTANT 500.00":
            scholarMDM = 500
        elif strMDMScholar == "PRESIDENT LIST 700.00":
            scholarMDM = 700
        elif strMDMScholar == "FULL SCHOLARSHIP 1000.00":
            scholarMDM = 1000
        elif strMDMScholar == "FULL SCHOLARSHIP 1000.00":
            scholarMDM = 1000
        elif strMDMScholar == "SELECT ONE":
            scholarMDM =0
        else:
            scholarMDM = 0

        amountToPayMDM = (tuitionMDM + regfeeMDM + intfeeMDM + idfeeMDM + libfeeMDM) - scholarMDM

        strMDMOutput = "<h3>OFFICIAL RECEIPT</h3>"
        strMDMOutput += "Student Number: " + strMDMSNumber + "<br>"
        strMDMOutput += "Student Name: " + strMDMLName + ", " + strMDMFName + " " + strMDMMName + "<br>"
        strMDMOutput += "Gender: " + strMDMGender + "<br>"
        strMDMOutput += "Email: " + strMDMEmail + "<br>"
        strMDMOutput += "Course: " + strMDMCourse + "<br>"
        strMDMOutput += "Amount To Pay: " + str("%.2f" % amountToPayMDM) + "<br>"

        return strMDMOutput
    return render_template("mp2-mod3-it106-mdm.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)