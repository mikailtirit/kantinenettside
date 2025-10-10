
# starter flask appen
from flask import Flask, render_template

# lager flask appen for kantinen
app = Flask (__name__)


@app.route('/') #forsiden
def index():
 return render_template("index.html")





