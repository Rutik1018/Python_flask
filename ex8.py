from flask import Flask,render_template

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('z_index.html')

@app.route('/friends/<name>')
def friend(name):
    return render_template('z_friends.html',name=name)

@app.route('/base')
def base():
    return render_template('z_base.html')

if __name__ == '__main__':
    app.run()