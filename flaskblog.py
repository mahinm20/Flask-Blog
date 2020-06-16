from flask import Flask,render_template,url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)