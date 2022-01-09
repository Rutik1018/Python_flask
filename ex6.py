# loops and conditions
from flask import Flask,render_template

app =Flask(__name__)

@app.route('/')                  #creating the basic pages
def index():
    list1=["tejas","Rutvik","ram","Sham"]
    return  render_template('two.html',list1 = list1)



if __name__ == '__main__':
    app.run(debug=True)