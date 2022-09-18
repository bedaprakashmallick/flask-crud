from distutils.log import error
from flask import Flask, url_for, request, redirect, render_template, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import os


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = os.urandom(24)
app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'scientia_innovation'

mysql = MySQL(app)

def get_current_user():
    Empuser = None
    if 'Empuser' in session:
        Empuser = session['Empuser']
        Emp = mysql.connection.cursor()
        Emp.execute("SELECT * FROM employee_details WHERE Email=%s", [Empuser])
        Empuser = Emp.fetchone()
    return Empuser

def all_employee():
    Emp = mysql.connection.cursor()
    Emp.execute("SELECT * FROM employee_details")
    AllEmployee = Emp.fetchall()

    return AllEmployee

        

@app.route("/")
def index():
    Empuser = get_current_user()
    return render_template("home.html", Empuser=Empuser)


@app.route("/login", methods=['GET', 'POST'])
def login():
    Empuser = get_current_user()
    if (Empuser != None):
        return redirect(url_for("dashboard"))
    error = ''
    if request.method == 'POST':
        Email = request.form['txtEmail']
        RawPassword = request.form['txtPassword']

        Emp = mysql.connection.cursor()
        Emp.execute("SELECT * FROM employee_details WHERE Email=%s", [Email])

        EmpDetails = Emp.fetchone()
        
        if (EmpDetails != None):
            Password = EmpDetails[-1]
            if (check_password_hash(Password, RawPassword)):
                session['Empuser'] = EmpDetails[3]
                return redirect(url_for('dashboard'))
            else:
                error = "Enter Correct Email and Password"
        else:
            error = 'Enter Correct Email and Password'
        return render_template("login.html", loginerror=error)
    return render_template("login.html", Empuser=Empuser)


@app.route("/register", methods=['GET', 'POST'])
def register():
    Empuser = get_current_user()
    if (Empuser != None):
        return redirect(url_for("dashboard"))
    error = ''
    if request.method == 'POST':
        EmployeeName = request.form['txtEmployeeName']
        Email = request.form['txtEmail']
        Designation = request.form['txtDesignation']
        Address = request.form['txtAddress']
        PhoneNo = request.form['txtPhoneNo']
        RawPassword = request.form['txtPassword']
        Password = generate_password_hash(RawPassword)

        if len(EmployeeName.strip()) and len(Email.strip()) and len(RawPassword.strip()):
            Emp = mysql.connection.cursor()
            Emp.execute("SELECT * FROM employee_details WHERE Email=%s", [Email])
            EmpDetails = Emp.fetchone()

            if (EmpDetails == None):
                Emp.execute("INSERT INTO employee_details(EmployeeName, Email, Designation, Address, Phone, Password) VALUES(%s, %s, %s, %s, %s, %s)", (EmployeeName, Email, Designation, Address, PhoneNo, Password))
                mysql.connection.commit()
                Emp.close()
                return redirect(url_for('login'))
            else:
                error = "(This Email is already exist.)"
                return render_template("register.html", Empuser=Empuser, loginerror=error)
        else:
            error = "(Do not Enter Blank name and email)"            
    return render_template("register.html", Empuser=Empuser, loginerror=error)


@app.route("/dashboard")
def dashboard():
    Empuser = get_current_user()
    AllEmployee = all_employee()
    return render_template("dashboard.html", Empuser=Empuser, AllEmployee=AllEmployee)


@app.route("/addnewemployee")
def addnewemployee():
    Empuser = get_current_user()
    return render_template("addnewemployee.html", Empuser=Empuser)


@app.route("/singleemployee")    
def singleemployeeprofile():
    Empuser = get_current_user()
    return render_template("singleemployee.html", Empuser=Empuser)


@app.route("/updateemployee", methods=["GET", "POST"])
def updateemployee():
    Empuser = get_current_user()
    error = ''
    if (request.method == "POST"):
        DbKey = request.form['hdnDbKey']
        EmployeeName = request.form['txtEmployeeName']
        Email = request.form['txtEmail']
        Designation = request.form['txtDesignation']
        Address = request.form['txtAddress']
        PhoneNo = request.form['txtPhoneNo']
        # RawPassword = request.form['txtPassword']
        # Password = generate_password_hash(RawPassword)

        if len(EmployeeName.strip()) and len(Email.strip()):
            Emp = mysql.connection.cursor()
            Emp.execute("UPDATE employee_details SET EmployeeName=%s, Email=%s, Designation=%s, Address=%s, Phone=%s WHERE DbKey=%s", (EmployeeName, Email, Designation, Address, PhoneNo, DbKey))
            mysql.connection.commit()
            Emp.close()
            return redirect(url_for('dashboard'))
        else:
            error = "Do Not Enter blank name, email and password"
    return render_template("updateemployee.html", Empuser=Empuser, error=error)


@app.route("/delete")
def deleteemployee():
    Empuser = get_current_user()
    EmpId = Empuser[0]
    Emp = mysql.connection.cursor()
    Emp.execute("DELETE FROM employee_details WHERE DbKey=%s", [EmpId])
    mysql.connection.commit()
    Emp.close()
    session.pop('Empuser', None)
    return redirect(url_for('dashboard'))



@app.route("/logout")
def logout():
    session.pop('Empuser', None)
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)