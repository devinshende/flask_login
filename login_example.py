from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, \
current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/sameer/Desktop/flask-login/login.db'
app.config['SECRET_KEY'] = 'thisissosecret'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True) # MUST be called id
	username = db.Column(db.String(30), unique=True)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@app.route('/')
def index():
	# request.get('username')
	print(type(User.query))
	user = User.query.fiter_by(username='Antonio').first()
	# login_user(user)	
	return 'Hello Antonio'

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return 'You are logged out'

@app.route('/home')
@login_required
def home():
	return 'The current user is ' + current_user.username


if __name__ == '__main__':
	app.run(debug=True)