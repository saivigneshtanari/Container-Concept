from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def get_vaccination_status():
    reg_no = request.form["reg_no"]
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="password",
        database="covid_vaccine"
    )
    cursor = db.cursor()
    query = "SELECT Vaccination_Status FROM Students WHERE RegNo = %s"
    cursor.execute(query, (reg_no,))
    result = cursor.fetchone()
    if result is None:
        vaccination_status = "Not Found"
    else:
        vaccination_status = result[0]
    db.close()
    return render_template("index.html", vaccination_status=vaccination_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

