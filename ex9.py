#this file creating basic page and othe r inheritate it
from flask import Flask,render_template,request

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('sign_index.html')


@app.route('/signup')
def signup():
    return render_template('sign_signup.html')

@app.route('/thankyou')
def thankyou():
    first=request.args.get('fisrt')
    last=request.args.get('last')
    return render_template('sign_thankyou.html',first=first,last=last)

if __name__ == '__main__':
    app.run(debug=True)