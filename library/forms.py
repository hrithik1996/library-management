from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, ValidationError,RadioField, DateTimeField,BooleanField,SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from datetime import date,timedelta
from library.models import User,Book,Book_issued

class admin(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')

class user(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')

class add_user(FlaskForm):
	First_name = StringField('First Name', validators=[DataRequired()])
	Last_name = StringField('Last Name', validators=[DataRequired()])
	username = StringField('Username', validators=[DataRequired()])
	contact_no = IntegerField('Contact', validators=[DataRequired()])
	adhaar_card = IntegerField('Adhaar' , validators=[DataRequired()])
	start_date = DateTimeField('Start Date', format="%Y-%m-%d",default=date.today, validators=[DataRequired()])
	end_date = DateTimeField('End Date', format="%Y-%m-%d", default=(date.today()+timedelta(days=365)))
	password = StringField('Password',validators=[DataRequired()])
	submit = SubmitField('Add')

	def validate_username(self,username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose another')

class add_book(FlaskForm):
	a = RadioField("",choices = [('B','Book'),('M','Movie')])
	book_name = StringField("Book Name", validators=[DataRequired()])
	author_name = StringField("Author Name", validators=[DataRequired()])
	pro_date = DateTimeField("Date of Procurement", format="%Y-%m-%d",default=date.today, validators=[DataRequired()])
	quantity = IntegerField("Quantity", validators=[DataRequired()])
	category = StringField("Category",validators=[DataRequired()])
	cost = IntegerField("Cost",validators=[DataRequired()])
	submit = SubmitField('Add')

class user_management(FlaskForm):
	b = RadioField(choices=[('N','New User'),('E','Existing User')])
	name = StringField("Name", validators=[DataRequired()])
	status = BooleanField('Status')
	admin = BooleanField('Admin')
	submit = SubmitField('Confirm')

class avail(FlaskForm):
	select = SelectField(u'Group',coerce=int)
	select_1 = SelectField(u'Group',coerce=int)
	submit = SubmitField('Search')

class issue_book(FlaskForm):
	book_name = SelectField(u'Group',coerce=int)
	author_name = StringField("Author Name", validators=[DataRequired()])
	issue_date = DateTimeField("Issue Date", format="%Y-%m-%d",default=date.today, validators=[DataRequired()])
	return_date = DateTimeField("Return Date",format="%Y-%m-%d",default=(date.today()+timedelta(days=365)))




