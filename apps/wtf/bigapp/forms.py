from flask.ext.wtf import Form, TextField, Required

class EmployeeForm(Form):
	first_name=TextField(validators=[Required()])
	last_name=TextField(validators=[Required()])