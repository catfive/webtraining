from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    def __repr__(self):
    	"""The default way records are represented"""
        return self.first_name

@app.route('/')
def home():
    """Home page"""
    return "hi"

@app.route('/employees')
def employee_list():
	"""A list of all employees"""
	employees = Employee.query.all()

	return render_template('employees.html',employees=employees)


if __name__ == '__main__':
    app.run()