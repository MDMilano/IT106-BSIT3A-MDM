from flask import Flask, render_template
appMDM = Flask(__name__)

@appMDM.route('/')
def indexMDM():
    return render_template("act1-mod3-it106-mdm.html")

if __name__ == "__main__":
    appMDM.run()