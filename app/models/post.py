from app import db
from .user import User

# One-To-Many
class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    text = db.Column(db.String(255))
    user_login = db.Column(
        db.String(50),
        db.ForeignKey('users.login'), #f'users.{User.login=}'.split('=')[0]
        # nullable=True,
    )
    
    def __repr__(self) -> str:
        return f'Post {self.text[:25]}'