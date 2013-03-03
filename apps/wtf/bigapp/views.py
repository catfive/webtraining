from flask import render_template, request
from models import Employee

def home():
    """Home page"""
    return "hi"


def employee_list():
    """A list of all employees"""
    employees = Employee.query.all()

    return render_template('employees.html', employees=employees)


def employee_add():
	"""Add an employee"""
	if request.method == 'POST':
		return 'form posted!'

	return render_template('employee_add.html', form=form)


def employee_update(id):
	"""Update employee record"""
	if request.method == 'POST':
		return 'form posted!'
	employee = Employee.query.get(id)
	
	return render_template('employee_add.html')