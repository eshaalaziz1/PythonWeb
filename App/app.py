from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.Config')


db = SQLAlchemy(app)


from routes import *


# create a database table
with app.app_context():
   db.create_all()


# this is the part the runs the server and the app
if __name__ == '__main__':
   app.run(debug=True)