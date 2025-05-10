from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    arrMDMCustomer = [
        ["001", "Di Magkamali", "Perfecto", "Regular", 500, 0.10, 0.03, 0.08],
        ["002", "Di Magilap", "Hassan", "Walk-In", 600, 0.12, 0.05, 0.07],
        ["003", "Di Matulac", "Dabiana", "Standard", 700, 0.11, 0.04, 0.06],
        ["004", "Di Mapacali", "Alberuto", "Delivery", 850, 0.09, 0.01, 0.05],
        ["005", "Di Mapasaya", "Sadner", "Walk-In", 1000, 0.12, 0.05, 0.06]
    ]
    strMDMProgBy = "Marc Daniel C. Milano"

    # Load templage page and provide parameter values
    return render_template('mp3-mod2-it106-mdm.html', customer=arrMDMCustomer, progby=strMDMProgBy)

if __name__ == "__main__":
    app.run(debug=True, port=1000)