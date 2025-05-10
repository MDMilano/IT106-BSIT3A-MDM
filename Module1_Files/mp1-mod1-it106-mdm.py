from flask import Flask
appMDM = Flask(__name__)

@appMDM.route("/")
#declare function for index
def indexMDM():
 #create variables and store strings to display
 strMDMCCSFP = ("<b><center><h1>City College of San Fernando<h1></center></b>"
                "<b><center><h3>City College of San Fernando<h3></b></center><br>")

 strMDMBPO= ("<b>BACHELOR'S PROGRAMS OFFERED</b><br>"
             "A. Bachelor of Science in Accountancy<br>"
             "B. Bachelor of Science in Business Management<br>"
             "C. Bachelor of Elementary Education Major in General Education<br>"
             "D. Bachelor of Secondary Education Major in Mathematics<br>"
             "E. Bachelor of Science in Information Technology<br>"
             "F. Bachelor Science in Hospitality Management<br>")

 strMDMBSPO = ("<br><b>SECONDARY PROGRAMS OFFERED</b><br>"
               "A. Elementary Education<br>"
               "B. Junior High School<br>"
               "C. Senior High School<br>")

 strMDMAR = ("<br><b>ADMISSION REQUIREMENTS</b><br>"
               "<b>Freshmen</b><br>"
               "1. Form 138<br>"
               "2. Certificate of good moral character<br>")

 strMDMTS = ("<br><b>Transfer Students</b><br>"
               "1. Honorable dismissal<br>"
               "2. Transcript of Records<br>"
               "3. Certificate of good moral character<br>")

 strMDMCUA = ("<br><footer><center><b>CONTACT US AT:</b></center></footer>"
              "<footer><center>Contact Number: 0917-123-4567 / 0916-143-4444</center></footer>"
              "<footer><center>Email Address: <a href=ccsfp-admission@yahoo.com>ccsfp-admission@yahoo.com</a> / <a href=ccsfp-admission@gmail.com>ccsfp-admission@gmail.com</a></center></footer>")

 #concatenate string variables
 strMDMOutput = strMDMCCSFP + strMDMBPO + strMDMBSPO + strMDMAR + strMDMTS + strMDMCUA
 #return strOutput to display in the webpage
 return strMDMOutput

if __name__ == "__main__":
 appMDM.run(debug=True, port=9000)