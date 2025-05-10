from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #Declare and initialize variables
    MDMName = "Marc Daniel C. Milano"
    MDMBDate = "March 15, 2004"
    MDMAdd = "City of San Fernando, Pampanga"
    MDMPrimary = "Malpitic Elementary School"
    MDMSecondary = "Sindalan High School"
    MDMTertiary = "City College of San Fernando"
    MDMCourse = "Bachelor of Science in Information Technology"
    MDMProgBy = "Marc Daniel C. Milano"

    #Load templage page and provide parameter values
    return render_template('Act1-Mod2-IT106-MDM.html', fName=MDMName, bDate=MDMBDate, \
                           add=MDMAdd, pri=MDMPrimary, sec=MDMSecondary, \
                           ter=MDMTertiary, cors=MDMCourse, progBy=MDMProgBy)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
