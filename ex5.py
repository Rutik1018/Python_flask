#connect one.html file to the python file
#also return the html file
from flask import Flask,render_template

app =Flask(__name__)

@app.route("/")
def index():
    return  render_template('one.html')



if __name__ == '__main__':
    app.run(debug=True)