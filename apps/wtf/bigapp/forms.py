from flask.ext.wtf import Form, TextField, required

class EmployeeForm(Form):
	first_name=TextField()
	last_name=TextField()