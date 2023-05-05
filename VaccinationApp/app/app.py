from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_vaccination_status", methods=["POST"])
def get_vaccination_status():
    reg_no = request.form["reg_no"]

    db = mysql.connector.connect(
        host="db",
        port="3306",
        user="root",
        password="password",
        database="covid_vaccine_db"
    )
    cursor = db.cursor()
    query = "SELECT vaccination_status FROM students WHERE reg_no = %s"
    cursor.execute(query, (reg_no,))
    result = cursor.fetchone()
    if result:
        return "Vaccination Status: {} thank you for being vaccinated!".format(result[0])
    else:
        return "Student not found."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

