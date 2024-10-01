from flask import Flask

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345@localhost:3306/test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




db = SQLAlchemy(app)
migrate = Migrate(app, db)



from controllers import *
from models import *
# from extensions import *

if __name__ == '__main__':
    app.run(debug=True)