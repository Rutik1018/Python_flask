from flask import Flask

app =Flask(__name__)

@app.route('/')                  #creating the basic pages
def hellow():
    return '<h1>Hellow World .....!!!! </h1>'



if __name__ == '__main__':
    app.run()