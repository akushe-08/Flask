from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import email_validator
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f4fac2f039c269ccfc46532ef1502c81'


posts = [
    {
        'author': 'Akshay Kalane',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'Oct 3, 2020'
    },

    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'Oct 4, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check Username and Password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
# if not using __name__ then "export FLASK_DEBUG=1" followed by "flask run"
