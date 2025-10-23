
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
    varer = [
        {"navn": "Bagett", "pris": "35kr", "bilde": "bagett.jpg"},
        {"navn": "Bolle", "pris": "20kr", "bilde": "bolle.jpg"},
        {"navn": "Drikke", "pris": "25kr", "bilde": "drikke.jpg"}
    ]
    return render_template("varer.html", varer=varer)

app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

  
  
  
if __name__ == "__main__":
    app.run(debug=True)






