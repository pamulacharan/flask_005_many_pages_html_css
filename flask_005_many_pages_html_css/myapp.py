from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/admin')
def admin():
    return render_template('admin.html', title='Admin')

@app.route('/user')
def user():
    return render_template('user.html', title='User')

if __name__ == '__main__':
    app.run(debug=True)
