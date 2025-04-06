from app import db
from datetime import datetime


class Student(db.Model):
   idnumber = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   grade_level = db.Column(db.String(50), nullable=False)
   email_address = db.Column(db.String(120), primary_key=True, unique=True, nullable=False)


   def __repr__(self):
       return f'Student({self.idnumber}, {self.name}, {self.grade_level}, {self.email_address})'