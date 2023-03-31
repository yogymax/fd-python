from config import db,app

class Person(db.Model):
    id = db.Column('user_id',db.Integer(),primary_key = True)
    firstname = db.Column('firstname', db.String(30))
    lastname = db.Column('lastname', db.String(30))
    email = db.Column('email', db.String(30),)
    gender = db.Column('gender', db.String(10))
    phone = db.Column('phone', db.String(10))

with app.app_context():
    db.create_all()
