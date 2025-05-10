from flask import Flask
app = Flask(__name__)

@app.route("/")
#declare function for index
def index():
    #create variables and store strings to display
    strPer = "<b>PERSONAL INFORMATION</b><br>"
    strName= "Name: Perfecto M. Di Magkamali<br>"
    strBDate ="Birthday: December 25, 1990<br>"
    strAdd ="Address: City of San Fernando, Pampanga<br><br>"
    strEduc ="<b>EDUCATIONAL BACKGROUND</b><br>"
    strPrimary="Primary: San Fernando Elementary School<br>"
    strSecondary = "Secondary: Pampanga National High School<br>"
    strTertiary= "Tertiary: Perfecture College of Art, Sciences and Technology<br>"
    strCourse = "Course: Bachelor of Science in Computer Science<br><br>"
    strProgBy ="Programmed by: Perfecto Di Magkamali<br>"
    #concatenate string variables
    strOutput = strPer + strName + strBDate + strAdd + strEduc + \
    strPrimary +  strSecondary + strTertiary + strCourse + strProgBy
    #return strOutput to display in the webpage
    return strOutput

if __name__ == "__main__":
    app.run()