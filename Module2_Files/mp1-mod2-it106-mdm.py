from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #arrMDM = [, , , , ]  ["", "", "", "", ""]
    arrMDMPNum = [1, 2, 3, 4, 5]
    arrMDMLName = ["Di Magkamali", "Di Magilap", "Di Matulac", "Dela Cruz", "Penduko"]
    arrMDMFName = ["Perfecto", "Hassan", "Dabiana", "Juan", "Pedro"]
    arrMDMAge = [2, 10, 25, 37, 60]
    arrMDMAGName = []
    arrMDMRType = ["W", "PR", "ICU", "SPR", "PICU"]
    arrMDMRPDay = [700, 900, 1200, 1000, 1500]
    arrMDMNoDays= [5, 7, 9, 11, 15]
    arrMDMLCharges = [1200, 1500, 1700, 2700, 300]
    arrMDMECharges = [500, 550, 600, 650, 700]
    strMDMProgBy = "Marc Daniel C. Milano"

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
        func = switcher.get(argument, lambda: "No Room Available")
        return func()

    for i in range(5):
        strMDMRDesc = getSwitch(arrMDMRType[i])

    for ctr in range(len(arrMDMAge)):
        if arrMDMAge[ctr] >= 0 and arrMDMAge[ctr] <=2:
            arrMDMAGName.append("Babies")
        elif arrMDMAge[ctr] >= 3 and arrMDMAge[ctr] <=16:
            arrMDMAGName.append("Children")
        elif arrMDMAge[ctr] >= 17 and arrMDMAge[ctr] <=30:
            arrMDMAGName.append("Young Adults")
        elif arrMDMAge[ctr] >= 31 and arrMDMAge[ctr] <=45:
            arrMDMAGName.append("Middle Aged Adults")
        elif arrMDMAge[ctr] > 45:
            arrMDMAGName.append("Old Adults")
        else:
            arrMDMAGName.append("Invalid Age")


    return render_template('mp1-mod2-it106-mdm.html', pnum=arrMDMPNum, lname=arrMDMLName,\
                           fname=arrMDMFName, age=arrMDMAge, agegroup=arrMDMAGName, rtype=arrMDMRType, rpday=arrMDMRPDay, nodays=arrMDMNoDays,\
                           labcharge=arrMDMLCharges, extcharge=arrMDMECharges, progby=strMDMProgBy)

if __name__ == "__main__":
    app.run(debug=True, port= 1000)


