import os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import os
from reader import retrieve_violation_data

PROJECT_DIR = os.getcwd()

f = PROJECT_DIR + '/static/data/violations.xls'


app = Flask(__name__)

@app.route("/")
def home():
    violations_data, total_violations = retrieve_violation_data(f)


    return render_template('home.html', violations_data=violations_data, total_violations=total_violations)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
