from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/welcome", methods=['POST'])
def welcome():
    user= request.form['username']
    pwd= request.form['password']
    verify_pwd = request.form['verify_password']
    email= request.form['email']
    if not user:
        error= "That's not a valid username"
        #return render_template("signup.html", usererror=error)
        return redirect("/?usererror="+error)

    return render_template('welcome.html',user=user)



def validate_user(username):
    if not username:
        return "That's not a valid username"
    else:
        if len(username)<3 or len(username)>20 or " " in username :
            return "That's not a valid username"
        return ""


def validate_password(password,verify_pwd):

    if password != verify_pwd or not password :
        return "The passwords dont match"

@app.route("/",methods=['POST','GET'])
def index():
    #encoded_error = request.args.get("error")
    if request.method =='GET':
        return render_template('signup.html')
    if request.method == 'POST':
        user= request.form['username']

        error= validate_user(user)
        pwd= request.form['password']
        verify_pwd=request.form['verify_password']
        verify_pwd_error= validate_password(pwd,verify_pwd)
        if not error and not verify_pwd_error:
            return render_template("welcome.html",user=user)
        return render_template("signup.html", usererror=error,verify_pwd_error=verify_pwd_error)
        
    return "nothing"

app.run()


