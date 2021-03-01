from flask import *
from DBManager import *
app = Flask(__name__)

db=DBManager()

@app.route('/')
def index():
    searchval=request.args.get("search")
    if searchval==None:
        lst=db.getAccList()
    else:
        lst=db.search(searchval)
    return render_template("index.html",alst=lst)

@app.route("/add")
def addAcc():
    nm=request.args["name"]
    bl=request.args["balance"]
    an=db.addAcc(nm,bl)
    msg="Account Opened. AccNo is "+str(an)
    return render_template("result.html",title="Open Account",msg=msg)


@app.route("/close")
def closeAcc():
    an=request.args["accno"]
    db.closeAcc(an)
    msg="Account Closed Successfully of AccNo "+an
    return render_template("result.html",title="Close Account",msg=msg)

@app.route("/deposit",methods=["GET","POST"])
def deposit():
    if request.method=="GET":
        an=request.args["accno"]
        rec=db.accInfo(an)
        return render_template("depositfrm.html",acc=rec)
    if request.method=="POST":
        an=request.form["accno"]
        amt=request.form["amt"]
        db.deposit(an,amt)
        return index()

@app.route("/withdraw",methods=["GET","POST"])
def withdraw():
    if request.method=="GET":
        an=request.args["accno"]
        rec=db.accInfo(an)
        return render_template("withdrawfrm.html",acc=rec)
    if request.method=="POST":
        an=request.form["accno"]
        amt=request.form["amt"]
        db.withdraw(an,amt)
        return index()


if __name__ == '__main__':
    app.run()
