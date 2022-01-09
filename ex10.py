from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app =Flask(__name__)

app.config['SECRET_KEY'] = 'Rutvik'                           #security key for app

class InfoForm(FlaskForm):                                   #creating the class for creating form name is optional and its fix type FlaskForm
    breed= StringField('What types of breed are you ? ')     #label with textarea   stringfield
    submit=SubmitField('Submit')                             #butoon submitfiled

@app.route('/',methods=['GET','POST'])
def index():
    breed = False                                                      # label column is empty
    form = InfoForm()                                                  #object of infoFORM
    if form.validate_on_submit():                                       # if click on submit
        breed = form.breed.data                                        # take data froom  label textarea
        form.breed.data=''                                             #making the data empty for new input
    return render_template('base.html',form=form,breed=breed)          #passing the variable


if __name__ == '__main__':
    app.run(debug=True)