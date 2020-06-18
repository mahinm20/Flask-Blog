from flask import Flask,render_template,url_for
from forms import RegistrationForm, LoginForm



app = Flask(__name__)
app.config['SECRET_KEY'] = 'b89285b701204bd2bad83b2e2f5b3ace'

posts = [
    {
        'author' : 'Mahin Malhotra',
        'title' : ' get schwifty',
        'content' : 'wubba lubba dub dub',
        'date_posted' : ' 16 June 2020'
    },
    {
        'author' : 'Darth Vader',
        'title' : ' Sith are awesome',
        'content' : 'join the dark side',
        'date_posted' : ' 16 June 2020'

    }
]

@app.route('/home')
@app.route('/')
def hello():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html',form=form,title='Register') 
 
# @app.route('/login')
# def register():
#     form = LoginForm()
#     return render_template('login.html',form=form,title='login')

if __name__ == '__main__':
    app.run(debug=True)