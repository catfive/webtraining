from bigapp import app
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)


class Job(db.Model):
	"""Job class/table

	title (string)"""

	id = db.Column(db.Integer(), primary_key=True)
	title = db.Column(db.String(50))


class Employee(db.Model):
    """The class/table for employee records

    first_name (string)
    last_name (string)"""
    
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    job_id = db.Column(db.Integer(), db.ForeignKey('Job'))
    job = db.relationship('Job')

    def __repr__(self):
        """The default way records are represented"""
        return self.first_name


