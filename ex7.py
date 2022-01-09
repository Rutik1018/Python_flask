#creating the variable and pass it and show it
from flask import Flask,render_template

app =Flask(__name__)

@app.route('/')                  #creating the basic pages
def index():
    name="Rutvik"                #variable
    list1=list(name)
    dict1={"Youtube":"markzookburg"}
    return render_template('three.html',name=name,list1=list1,dict1=dict1)



if __name__ == '__main__':
    app.run(debug=True)