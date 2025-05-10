from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #Declare and initialize variables
    strMDMLName = "Milano"
    strMDMFName = "Marc Daniel"
    strMDMMName = "Candule"
    dblMDMPre = 80
    dblMDMMid = 85
    dblMDMFin = 90
    strMDMProgBy = "Marc Daniel C. Milano"
    #Concatenate names
    strMDMFullName = strMDMLName + ", " + strMDMFName + " " + strMDMMName
    #Compute subject grade
    dblMDMSGrade = (dblMDMPre + dblMDMMid + dblMDMFin)/3


#Apply If and Else Statement to determine Remarks
    if dblMDMSGrade > 74:
        strMDMRemarks = "Passed!"
    else:
        strMDMRemarks = "Failed"

#Apply If and Elif Statement to determine Ratings
    if dblMDMSGrade >= 98 and dblMDMSGrade <= 100:
        strMDMRatings = "Excellent!"
    elif dblMDMSGrade >= 92 and dblMDMSGrade <= 97:
        strMDMRatings = "Very Good!"
    elif dblMDMSGrade >= 83 and dblMDMSGrade <= 91:
        strMDMRatings = "Good!"
    elif dblMDMSGrade >= 78 and dblMDMSGrade <= 82:
        strMDMRatings = "Fair!"
    elif dblMDMSGrade >= 75 and dblMDMSGrade <= 77:
        strMDMRatings = "Satisfactory!"
    else:
        strMDMRatings = "Poor!"

#Creating the functions for Switcher selections
    def bscs():
        strMDMCourse = "Bachelor of Science in Computer Science"
        return strMDMCourse

    def bsit():
        strMDMCourse = "Bachelor of Science in Information Technology"
        return strMDMCourse

    def bsis():
        strMDMCourse = "Bachelor of Science in Information Systems"
        return strMDMCourse

#Switch Case Statement
    switcher = {
        "BSCS": bscs,
        "BSIT": bsit,
        "BSIS": bsis
    }

    def getSwitch(argument):
        # Get the function from the switcher dictionary
        func = switcher.get(argument, lambda: "No Course Available")
        return func()

    strMDMCorCode = "BSIT"
    strMDMCorDept = getSwitch(strMDMCorCode)

#Load templage page and provide parameter values
    return render_template('Act2-Mod2-IT106-MDM.html', fullName=strMDMFullName, pre=dblMDMPre, \
                           mid=dblMDMMid, fin=dblMDMFin, sgrade=dblMDMSGrade, rem=strMDMRemarks, \
                           rate=strMDMRatings, cors=strMDMCorDept, progBy=strMDMProgBy)


if __name__ == "__main__":
    app.run(debug=True, port=8000)