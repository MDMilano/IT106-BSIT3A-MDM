from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # Declare and initialize multi dimensional array
    arrMDMStudGrade = [
    ["Di Magkamali","Perfecto", "First Year","BS Computer Science",85, 90, 95],
    ["Di Matulac", "Hebili", "Second Year", "BS Information Technology", 86, 87, 88],
    ["Di Magiba", "Bogart", "Third Year",  "BS Information Science", 90, 92, 93],
    ["Di Mapakali", "Alberuto", "Fourth Year", "BS Computer Science", 80, 83, 86],
    ["Di Mahanap", "Hassan", "Fourth Year",  "BS Information Technology", 70, 72, 74]
    ]
    strMDMProgBy = "Marc Daniel C. Milano"

# Load templage page and provide parameter values
    return render_template('act4-mod2-it106-mdm.html', studgrade=arrMDMStudGrade, progBy=strMDMProgBy)

if __name__ == "__main__":
    app.run(debug=True, port=7002)