
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

if __name__ == "__main__":
    app.run(debug=True)






