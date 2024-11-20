from flask import Flask
from flask import render_template,request

app=Flask(__name__)

#@app.route("/",methods=["GET","POST"])
#def index():
 #   return(render_template("index.html"))

#@app.route("/",methods=["GET","POST"])
#def main():
 #   name=request.form.get("q")
 #   return(render_template("main.html"))

@app.route("/",methods=["GET","POST"])
def answer1():
    return(render_template("answer1.html"))

if __name__=="__main__":
    app.run()
