from flask import Flask, url_for, request
app = Flask(__name__)

# @app.route('/')
# def index():
# 	return "Index!"

# @app.route('/hello')
# def hello():
# 	return 'Hellow World!'

# @app.route('/<the_goods>')
# def the_goods(the_goods):
# 	return "You that {0}".format(the_goods)

# @app.route('/endpoint/')
# def test_endpoint():
# 	return "Here it is, the endpoint!"

# @app.route('/')
# def index(): pass

# @app.route('/login')
# def login(): pass

# @app.route('/user/<user_name>')
# def profile(user_name): pass

# with app.test_request_context():
# 	print url_for('index')
# 	print url_for('login')
# 	print url_for('login', next='/')
# 	print url_for('profile', user_name='John Doe')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		show_the_login_form()

@app.route('/login/input')
def show_the_login_form():
	return "Here's the login form"

@app.route('/login/input/snoze')
def do_the_login():
	return "Here's the login doitz"




if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)