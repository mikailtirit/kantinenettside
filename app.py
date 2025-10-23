
# starter flask appen
from flask import Flask, render_template

# lager flask appen for kantinen
app = Flask (__name__)


@app.route('/') 
def index():
    return render_template('index.html')


@app.route("/meny")
def meny():
    ukens_meny = [
        "Mandag: karbonade og poteter",
        "Tirsdag: Hannas lassagne",
        "Onsdag: Taco",
        "Torsdag: Toast",
        "Fredag: pannekaker"
]
    return render_template("meny.html", ukens_meny=ukens_meny)


@app.route("/varer")
def varer():
    faste_varer = [
        {"navn": "Bagett", "pris": "35kr"},
        {"navn": "Bolle", "pris": "20kr"},
        {"navn": "Drikke", "pris": "25kr"}
    ]
    return render_template("varer.html", faste_varer=faste_varer)


  
  
  
if __name__ == "__main__":
    app.run(debug=True)






