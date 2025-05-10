from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    arrMDMENum = ["001", "002", "003", "004", "005"]
    arrMDMLName = ["Di Magkamali", "Di Magilap", "Di Matulac", "Dela Cruz", "Penduko"]
    arrMDMFName = ["Perfecto", "Hassan", "Dabiana", "Juan", "Pedro"]
    arrMDMRPDay = [1250, 1300, 1350, 1400, 1450]
    arrMDMRPHour = [125, 150, 175, 200, 250]
    arrMDMNoDays = [5, 7, 9, 11, 15]
    arrMDMEHours = [2, 4 ,6, 8, 10]
    arrMDMEAmenities = [500, 550, 600, 650, 700]
    strMDMProgBy = "Marc Daniel C. Milano"

    arrMDMRType = {
        "RR": "Regular Room",
        "SR": "Suite Room",
        "ER": "Executive Room",
        "PR": "Presidential Room"
    }

    arrMDMTAmount = []
    for ctr in range(len(arrMDMENum)):
        dblMDMTAmount = (arrMDMRPDay[ctr] * arrMDMNoDays[ctr]) + (arrMDMRPHour[ctr] * arrMDMEHours[ctr]) + arrMDMEAmenities[ctr]
        arrMDMTAmount.append(dblMDMTAmount)

    return render_template('mp2-mod2-it106-mdm.html', enum=arrMDMENum, lname=arrMDMLName, \
                           fname=arrMDMFName, rpday=arrMDMRPDay, rphour=arrMDMRPHour, nodays=arrMDMNoDays, \
                           ehours=arrMDMEHours, eamenities=arrMDMEAmenities, rtype=arrMDMRType, \
                           tamount=arrMDMTAmount, progby=strMDMProgBy)

if __name__ == '__main__':
    app.run(debug=True, port=1000)