from app import db

class User(db.Model):
    __tablename__ = "users"

    login = db.Column(
        db.String(50),
        primary_key=True,
    )
    posts = db.relationship(
        'Post',
        backref=__tablename__,
        cascade="all, delete"
    )

    def __repr__(self) -> str:
        return f'User {self.login} posts:{[x for x in self.posts]}'

