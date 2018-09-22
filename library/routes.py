from flask import Flask, render_template, redirect, url_for, request,flash
from library import app, db, bcrypt
from library.forms import admin, user, add_user, add_book,user_management,avail
from library.models import Admin,User,Book,Book_issued
from flask_login import login_user
@app.route("/")
@app.route("/library")
def library():
	return render_template('main.html')

@app.route("/admin_login", methods=['GET','POST'])
def admin_login():
	form = admin()
	if form.validate_on_submit():
		admin1 = Admin.query.filter_by(username=form.username.data).first()
		if admin1 and bcrypt.check_password_hash(admin1.password, form.password.data):
			login_user(admin1)
			return redirect(url_for('admin_home'))
		else:
			flash('Login Unsuccesful')


	return render_template('login_admin.html', form=form)

@app.route("/user_login", methods=['GET','POST'])
def user_login():
	form = user()
	if form.validate_on_submit():
		user1 = User.query.filter_by(username=form.username.data).first()
		if user1 and bcrypt.check_password_hash(user1.password, form.password.data):
			login_user(user1)
			return redirect(url_for('user_home'))
		else:
			flash('Login Unseccesful')
	return render_template('login_user.html', form=form)


@app.route("/user_home")
def user_home():
	return render_template('user_home.html')

@app.route("/admin_home")
def admin_home():
	return render_template('admin_home.html')
 
@app.route("/maintenance")
def maintenance():
	return render_template('maintenance.html')

@app.route("/report")
def report():
	return render_template('report.html')

@app.route("/transaction")
def transaction():
	return render_template('transaction.html')


@app.route("/add_member",methods=['GET','POST'])
def adduser():
	form=add_user()
	if form.validate_on_submit():
	    user = User(first_name=form.First_name.data,last_name=form.Last_name.data,username=form.username.data,contact_no=form.contact_no.data,adhaar_card=form.adhaar_card.data,start_date=form.start_date.data,end_date=form.end_date.data,password=form.password.data)
	    db.session.add(user)
	    db.session.commit()
	    flash('account created','success')
	    return redirect(url_for('maintenance'))
	return render_template('add_membership.html',form=form)


@app.route("/add_book",methods=['GET','POST'])
def addbook():
	form = add_book()
	if form.validate_on_submit():
		book = Book(book_name=form.book_name.data,author_name=form.author_name.data,pro_date=form.pro_date.data,quantity=form.quantity.data,category=form.category.data,cost=form.cost.data)
		db.session.add(book)
		db.session.commit()
		flash('Book added','success')
		return redirect(url_for('maintenance'))
	return render_template('add_book.html',form=form)

@app.route("/user_management",methods=['GET','POST'])
def usermanage():
	form = user_management()
	if form.validate_on_submit():
		if form.b.data == 'E':
		    user = User.query.filter_by(username=form.name.data).first()
		if admin:
			admin_1 = Admin(username=User.username,first_name=User.first_name,last_name=User.last_name,password=User.password)
			db.session.add(admin_1)
			db.session.commit()
		return redirect(url_for('admin_home'))
	return render_template('user_management.html',form=form)	
			


		
@app.route("/master_books")
def masterbooks():
	books = Book.query.all()
	return render_template('masterbooks.html',books=books)

@app.route("/master_membership")
def mastermember():
	users = User.query.all()
	return render_template('mastermember.html',users=users)



@app.route("/available_book",methods=['GET','POST'])
def available():
	book = Book.query.all()
	form = avail(obj=book)
	form.select.choices = [(g.id,g.book_name) for g in Book.query.order_by('book_name')]
	form.select_1.choices = [(a.id,a.author_name) for a in Book.query.order_by('author_name')]
	if form.validate_on_submit():
		return redirect(url_for('search'))
	return render_template('available_book.html',form = form,book=book)

@app.route("/search")
def search():
	return render_template('search.html')