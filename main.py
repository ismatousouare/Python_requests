import requests
from flask import Flask,render_template
app  = Flask(__name__)
@app.route("/countries")
def getCountries():
    r = requests.get('https://restcountries.com/v3.1/name/guinea')
    return render_template("index.html",info=r.text,code_retour=r.status_code)
@app.route("/pays")
def getPays():
    r = requests.get('https://restcountries.com/v3.1/name/guinea')
    return render_template("pays.html",r=r)

if __name__ =='__main__':
    app.run(debug=True);