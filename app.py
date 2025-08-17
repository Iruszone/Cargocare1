from flask import Flask, render_template,request,url_for,session,redirect,flash
from flask_mysqldb import MySQL
import random
import string


app = Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="hpserver"
app.config["MYSQL_DB"]="cargocare"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST" and 'apply' in request.form:
        pickup = request.form["pickup"]
        dropoff = request.form["dropoff"]
        date = request.form["date"]
        time = request.form["time"]

        cur = mysql.connection.cursor()
        cur.execute(' insert into booking (pickup,dropoff,date,time) values (%s, %s, %s, %s)',
                                            [pickup,dropoff,date,time])
        mysql.connection.commit()
        
        cur.close()

        return redirect(url_for("index"))
    
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if 'alogin' in request.form:
        if request.method == 'POST':
            aname = request.form["aname"]
            apass = request.form["apass"]
            try:
                cur = mysql.connection.cursor()
                cur.execute("select * from login where aname=%s and apass=%s", [aname, apass])
                res = cur.fetchone()
                if res:
                    session["aname"] = res["aname"]
                    session["aid"] = res["aid"] 
                    flash("Login successful!", "success")
                    return redirect(url_for('index'))
                else:
                    flash("Invalid username or password!", "danger")
                    return render_template("login.html")
            except Exception as e:
                print(f"Error during login: {e}")
                flash("An error occurred. Please try again later.", "danger")
            finally:
                cur.close()

    return render_template("login.html")

@app.route("/sign",methods=['GET','POST'])
def sign():
    if request.method == "POST" and 'signup' in request.form:
        aname = request.form["aname"]
        semail = request.form["semail"]
        apass = request.form["apass"]
        sconfirm = request.form["sconfirm"]

        cur = mysql.connection.cursor()
        cur.execute(' insert into login (aname,semail,apass,sconfirm) values (%s, %s, %s, %s)',
                                            [aname,semail,apass,sconfirm])
        mysql.connection.commit()
        
        cur.close()
        return redirect(url_for("login"))    
    return render_template("sign.html")

        
@app.route("/ccc")
def ccc():
    return render_template("ccc.html")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # Clear the session data
    session.clear()
    # Redirect to the login page
    return redirect(url_for('login'))

@app.route("/register",methods=['GET','POST'])
def registration():
    if request.method == "POST" and 'register' in request.form:
        rname = request.form["rname"]
        remail = request.form["remail"]
        rphone = request.form["rphone"]
        rdob = request.form["rdob"]
        rlicence = request.form["rlicence"]
        rlicence_expiry_date = request.form["rlicence_expiry_date"]
        rinsurance = request.form["rinsurance"]
        rvehicle_make = request.form["rvehicle_make"]
        rvehicle_model = request.form["rvehicle_model"]
        rvehicle_year = request.form["rvehicle_year"]
        rvehicle_registration = request.form["rvehicle_registration"]
        
        cur = mysql.connection.cursor()
        cur.execute(' insert into driver_registration (rname,remail,rphone,rdob,rlicence,rlicence_expiry_date,rinsurance,rvehicle_make,rvehicle_model,rvehicle_year,rvehicle_registration) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                            [rname,remail,rphone,rdob,rlicence,rlicence_expiry_date,rinsurance,rvehicle_make,rvehicle_model,rvehicle_year,rvehicle_registration])
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("ccc"))
    return render_template("registration.html")

   
@app.route("/status")
def status():
    return render_template("status.html")

@app.route("/driver_status")
def driver_status():
    return render_template("driver_status.html")

@app.route("/book", methods=["POST"])
def book():
    if "aname" not in session:
        return {"status": "login_required"}, 401


if __name__ == "__main__":
    app.secret_key='123'
    app.run(debug=True)

