from flask import render_template
from models import Employee
from forms import EmployeeForm

def home():
    """Home page"""
    return "hi"


def employee_list():
    """A list of all employees"""
    employees = Employee.query.all()

    return render_template('employees.html', employees=employees)


def employee_add():
	"""Add an employee"""
	form = EmployeeForm()
	return render_template('employee_add.html', form=form)