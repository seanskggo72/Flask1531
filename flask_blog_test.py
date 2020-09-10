# Last modify: Aug 25

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)  # __name__ is same as __main__ special variable

app.config['SECRET_KEY'] = '4c956acf28b2bcdeeb2e90059797cf90'


posts = [
	{
		'author': 'User 1',
		'title': 'Post 1',
		'content': 'First test',
		'date': '24 Aug 2020'
	},
	
	{
		'author': 'User 2',
		'title': 'Post 2',
		'content': 'second test',
		'date': '24 Aug 2020'
	}
]

# decorators route, `/' is the root page of the website
@app.route('/')
@app.route('/home') 
def home():
    return render_template('home.html', posts = posts)
    
    # opened export FLASK_APP=flask_blog_test.py (file name)
    # for a quicker run for the program
    # by "flask run" command
    # setup the debug mode for flask
    # "export FLASK_DEBUG=1" in commandline 
    # in windows, use "set" rather than "export"

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'Success')
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in !', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful', 'danger')
			
	return render_template('login.html', title = 'Login', form = form)

# open the debug mode as well...
if __name__ == '__main__':
	# if wanna use python to directly open the program, dont use python
	# use python3 instead
	app.run(debug=True)
