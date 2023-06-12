from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def hi():
    if(request.form):
       clicked=request.form["btn"]
       if(clicked=="incbtn"):
          return render_template("formincome.html")
       elif(clicked == 'emibtn'):
           return render_template("emical.html")
       elif(clicked == 'gstbtn'):
            return render_template("gstcalc.html")
       elif(clicked == 'backbtn'):
            return render_template("index.html")
        
   
    return render_template("index.html")
      


if __name__=='__main__':
    app.run(debug=True,port=5144)


