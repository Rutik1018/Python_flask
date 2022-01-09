from flask import Flask,render_template
app =Flask(__name__)

@app.route("/")    #end point
def hello():
    myname1="Rutvik"
    return  render_template('bt.html',  name =myname1)

app.run(debug=True)