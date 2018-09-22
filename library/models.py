from datetime import datetime,timedelta,date
from library import db, login_manager
from flask_login import UserMixin
from library import bcrypt

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class Admin(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	first_name = db.Column(db.String(20),nullable=False)
	last_name = db.Column(db.String(20),nullable=False)
	password = db.Column(db.String(60), nullable=False)
	updation_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
	
	def __init__(self, username,first_name,last_name, password):
		self.username=username
		self.first_name=first_name
		self.last_name=last_name
		self.password=bcrypt.generate_password_hash(password)

	def __repr__(self):
		return f"Admin('{self.username}','{self.first_name}','{self.last_name}')"


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20),nullable=False)
	last_name = db.Column(db.String(20),nullable=False)
	username = db.Column(db.String(20),unique=True,nullable=False)
	contact_no = db.Column(db.Integer, unique=True)
	adhaar_card = db.Column(db.Integer,unique=True)
	start_date = db.Column(db.DateTime, nullable=False)
	end_date = db.Column(db.DateTime, nullable=False)
	password = db.Column(db.String(60),nullable=False)
	user_issue = db.relationship('Book_issued', backref='user_issue', lazy=True)

	def __init__(self,first_name,last_name,username,contact_no,adhaar_card,start_date,end_date,password):
		self.first_name=first_name
		self.last_name=last_name
		self.username=username
		self.contact_no=contact_no
		self.adhaar_card=adhaar_card
		self.start_date=start_date
		self.end_date=end_date
		self.password=bcrypt.generate_password_hash(password)

	def __repr__(self):
		return f"User('{self.username}','{self.first_name}','{self.last_name}','{self.contact_no}','{self.adhaar_card}','{self.start_date}','{self.end_date}')"

class Book(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	book_name = db.Column(db.String(20),nullable=False)
	author_name = db.Column(db.String(20),nullable=False)
	pro_date = db.Column(db.DateTime,nullable=False,default=date.today)
	quantity = db.Column(db.Integer, nullable=False,default=1)
	category = db.Column(db.String(20),nullable=False)
	cost = db.Column(db.Integer,nullable=False)
	issue = db.relationship('Book_issued',backref='book_issue', lazy=True)

	def __init__(self,book_name,author_name,pro_date,quantity,category,cost):
		self.book_name=book_name
		self.author_name=author_name
		self.pro_date=pro_date
		self.quantity=quantity
		self.category=category
		self.cost=cost

	def __repr__(self):
		return f"book('{self.id}','{self.book_name}','{self.author_name}','{self.pro_date}','{self.quantity}','{self.category}','{self.cost}')"



class Book_issued(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	issue_date = db.Column(db.DateTime, nullable=False, default=date.today)
	return_date = db.Column(db.DateTime,nullable=False, default=(date.today() + timedelta(days=10)))
	fine = db.Column(db.String(20))


	def __repr__(self):
		return f"book_issued('{self.book_id}','{self.user_id}','{self.issue_date}','{self.return_date}','{self.fine}')"



