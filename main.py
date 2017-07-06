from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/welcome")
def welcome():
    user= request.args.get("username")
    #user= request.form['username']
    #pwd= request.form['password']
    #verify_pwd = request.form['verify_password']
    #email= request.form['email']
    return render_template('welcome.html',user=user)



def validate_user(username):
    if not username:
        return "That's not a valid username"
    else:
        if len(username)<3 or len(username)>20 or " " in username :
            return "That's not a valid username"
        return ""


def validate_password(password):

    if not password :
        return "That's not a valid password"
    else:
        if len(password)<3 or len(password)>20 or " " in password :
            return "That's not a valid password"

        else:
            return ""    

def verify_passwords(password,verify_pwd):
    if password != verify_pwd:
        return "The passwords dont match"
    else:
        return "" 

def validate_email(email):
    if not email:
        return ""
    else:
        if len(email)<3 or len(email)>20:
            return "That's not a valid email"
        else:
            pattern = r"^[a-zA-Z0-9+-_!.]+@[a-zA-Z0-9]+\.[a-z]+[.]*[a-z]*$"
            matchstring = re.match(pattern,email)
            if matchstring:
                return ""
            else:
                return "That's not a valid email"        



@app.route("/",methods=['POST','GET'])
def index():
    #encoded_error = request.args.get("error")
    if request.method =='GET':
        return render_template('signup.html')
    if request.method == 'POST':
        user= request.form['username']

        user_error= validate_user(user)
        pwd= request.form['password']
        pwd_error= validate_password(pwd)
        email= request.form['email']
        email_error = validate_email(email)
        verify_pwd=request.form['verify_password']
        verify_pwd_error= verify_passwords(pwd,verify_pwd)
        if not user_error and not verify_pwd_error and not pwd_error and not email_error:
            #return render_template("welcome.html",user=user)
            return redirect("/welcome?username="+user)
        
        return render_template("signup.html", usererror=user_error,verify_pwd_error=verify_pwd_error, pwd_error= pwd_error, email_error=email_error, username=user, email=email)
        
    return "something wrong"

app.run()


