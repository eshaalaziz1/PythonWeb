from flask import Flask


# calls instance of class.
app = Flask(__name__)
app.config.from_object('config.Config')
# this import comes later because the previous code is required for route
from routes import *

# is only called on run
if __name__ == '__main__':
    app.run(debug=True)