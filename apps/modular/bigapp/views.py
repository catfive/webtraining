from flask import render_template
from models import Employee

def home():
    """Home page"""
    return "hi"


def employee_list():
    """A list of all employees"""
    employees = Employee.query.all()

    return render_template('employees.html',employees=employees)