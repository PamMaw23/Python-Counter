from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] +=1
    return render_template("index.html")

@app.route('/count', methods = ["POST"])
def one_count():
    if request.form["change"]=="add": #this will add to the counter as the add button is clicked
        session["count"]+=1
    elif request.form["change"]=="reset":
        session["count"]=0 #this will reset the counter to 1 when the reset button is clicked
    return redirect("/") #cannot put render_template under POST

@app.route('/destroy')
def destroy():
    session.clear() #this will clear previous count
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)