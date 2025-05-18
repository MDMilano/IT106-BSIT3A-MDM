from flask import Flask, render_template
from flask import request
appMDM = Flask(__name__)

@appMDM.route('/', methods=["GET", "POST"])
def indexMDM():
    if request.method == "POST":
        # GET USER INPUT
        strMDMID = request.form["Student_ID"]
        strMDMName = request.form["Student_Name"]
        dblMDMPre = request.form["Prelim_Grade"]
        dblMDMMid = request.form["Midterm_Grade"]
        dblMDMFin = request.form["Final_Grade"]

        # PROCESS INPUTS - COMPUTATION
        dblMDMSGrade = (float(dblMDMPre) + float(dblMDMMid) + float(dblMDMFin)) / 3
        # appMDMly If and Else Statement to determine Remarks
        if dblMDMSGrade > 74:
            strMDMRemarks = "Passed!"
        else:
            strMDMRemarks = "Failed"

        # appMDMly If and Elif Statement to determine Ratings
        if dblMDMSGrade > 97 and dblMDMSGrade <= 100:
            strMDMRatings = "Excellent!"
        elif dblMDMSGrade > 91 and dblMDMSGrade <= 97:
            strMDMRatings = "Very Good!"
        elif dblMDMSGrade > 82 and dblMDMSGrade <= 91:
            strMDMRatings = "Good!"
        elif dblMDMSGrade > 77 and dblMDMSGrade <= 82:
            strMDMRatings = "Fair!"
        elif dblMDMSGrade >= 75 and dblMDMSGrade <= 77:
            strMDMRatings = "Satisfactory!"
        else:
            strMDMRatings = "Poor!"

        strMDMOutput = "<h3>GRADE SLIP</h3>" \
                    "Student Number: " + strMDMID + "<br>" \
                    "Student Name: " + strMDMName + "<br>" \
                    "Prelim Grade: " + dblMDMPre + "<br>" \
                    "Midterm Grade: " + dblMDMMid + "<br>" \
                    "Final Grade: " + dblMDMFin + "<br>" \
                    "Subject Grade: " + str(dblMDMSGrade) + "<br>" \
                    "Remarks: " + strMDMRemarks + "<br>" \
                    "Ratings: " + strMDMRatings + "<br>"

        return strMDMOutput
    return render_template("act2-mod3-it106-mdm.html")

if __name__ == "__main__":
    appMDM.run()