from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.settings import Settings

app = Flask(__name__)

# Налаштування 
app.config.from_object(Settings)
db = SQLAlchemy(app)

# Міграція
migrate = Migrate(
    app=app,
    db=db
)

# app_users = Flask(__name__)

# Налаштування 
# app_users.config.from_object(Settings)

# db_users = SQLAlchemy(app_users)

# migrate_users = Migrate(
#     app=app_users,
#     db=db_users
# )
from app import models, routes

# with app.app_context():
#     db.create_all()