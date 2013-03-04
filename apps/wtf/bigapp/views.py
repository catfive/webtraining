from flask import render_template, request
from models import db, Employee
from forms import EmployeeForm


def home():
    """Home page"""
    
    return render_template('home.html')


def employee_list():
    """A list of all employees"""
    employees = Employee.query.all()

    return render_template('employees.html', employees=employees)


def employee_add():
	"""Add an employee"""
	if request.method == 'POST':
		form = EmployeeForm(request.form)
		new_employee = Employee()
		form.populate_obj(new_employee)
		db.session.add(new_employee)
		db.session.commit()
		return 'Employee added!'
	form = EmployeeForm()

	return render_template('form.html', form=form)


def employee_update(id):
	"""Update employee record"""
	employee = Employee.query.get(id)
	form = EmployeeForm(obj=employee)

	if request.method == 'POST':
		form.populate_obj(employee)
		db.session.commit()
		return 'Employee updated!'

	return render_template('form.html', form=form)
