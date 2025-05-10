from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #Declare and initialize single dimensional array
    arrMDMLName = ["Di Magkamali", "Di Mahagilap", "Di Matulac", "Di Mahanap", "Di Mapakali"]
    arrMDMFName = ["Perfecto", "Hassan", "Dabiana", "Ditolado", "Albereto"]
    arrMDMPre = ["90", "91", "92", "93", "94"]
    arrMDMMid = ["80", "81", "82", "83", "84"]
    arrMDMFin = ["75", "80", "85", "90", "95"]
    strMDMProgBy = "Marc Daniel C. Milano"

    #Declare and initialize dictionaries
    arrMDMLevel = {"First":"First Year",
                "Second":"Second Year",
                "Third":"Third Year",
                "Fourth":"Fourth Year"
                }

    arrMDMCourse = {"BSCS":"BS in Computer Science",
                 "BSIT":"BS in Information Technology",
                 "BSIS":"BS in Information Systems"
                 }

    # Load templage page and provide parameter values
    return render_template('act3-mod2-it106-mdm.html', level=arrMDMLevel, cors=arrMDMCourse, \
                           lname=arrMDMLName, fname=arrMDMFName, pre=arrMDMPre, mid=arrMDMMid,
                           fin=arrMDMFin, progBy=strMDMProgBy)

if __name__ == "__main__":
    app.run(debug=True, port= 7001)