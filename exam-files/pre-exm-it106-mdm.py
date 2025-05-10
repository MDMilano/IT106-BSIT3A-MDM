from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    arrMDMEmployees = [
        ["001", "Di Magkamali", "Perfecto", "S1", 150, 30, 1, 10],
        ["002", "Di Magilap", "Hassan", "S1", 200, 35, 2, 25],
        ["003", "Di Matulac", "Dabiana", "S1", 250, 100, 3, 20],
        ["004", "Di Mapacali", "Alberuto", "S1", 300, 200, 4, 30],
        ["005", "Di Mapasaya", "Sadner", "S1", 350, 300, 5, 25]
    ]
    strMDMProgBy = "Marc Daniel C. Milano"

    # Load template page and provide parameter values
    return render_template('pre-exm-it106-mdm.html', customer=arrMDMEmployees, progby=strMDMProgBy)

if __name__ == "__main__":
    app.run(debug=True, port=1000)