#debug mode
from flask import Flask

app =Flask(__name__)

@app.route('/')                            #creating the basic pages
def hellow():
    return '<h1>Hellow World .....!!!! </h1>'

@app.route('/info')
def info():
    return '<h3> inforamation about the my webpage <\h3>'

@app.route('/friend/<name>')               #name pasiing the arguments
def friend(name):
    return 'last character of my name is --> {}'.format(name[-1])

if __name__ == '__main__':
    app.run(debug=True)                    #debug is true because it tell us why error is showing