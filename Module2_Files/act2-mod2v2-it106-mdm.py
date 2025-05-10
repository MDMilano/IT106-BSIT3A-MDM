from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #Declare and initialize variables
    strMDMLName = "Milano"
    strMDMFName = "Marc Daniel"
    strMDMMName = "Candule"
    dblMDMPre = 90
    dblMDMMid = 95
    dblMDMFin = 90
    strMDMProgBy = "Marc Daniel C. Milano"
    #Concatenate names
    strMDMFullName = strMDMLName + ", " + strMDMFName + " " + strMDMMName

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
    return render_template('Act2-Mod2V2-IT106-MDM.html', fullName=strMDMFullName, pre=dblMDMPre, \
                           mid=dblMDMMid, fin=dblMDMFin, cors=strMDMCorDept, progBy=strMDMProgBy)

if __name__ == "__main__":
    app.run(debug=True, port=8000)