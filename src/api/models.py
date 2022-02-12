from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#    def serialize(self):
#        return {
#            "id": self.id,
#            "email": self.email,
#            # do not serialize the password, its a security breach
#       }


class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

class Character(db.Model):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    age = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    specie = db.Column(db.String(250))

class Planet(db.Model):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    population = db.Column(db.Integer)

class Favorite(db.Model):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    character=db.relationship(Character)
    user=db.relationship(User)
    planet=db.relationship(Planet)