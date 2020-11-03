from flask import Flask, render_template, url_for
app = Flask(__name__)

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
def about_page():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
# if not using __name__ then "export FLASK_DEBUG=1" followed by "flask run"
