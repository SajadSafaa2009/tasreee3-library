from app import db


class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    general_type = db.Column(db.Boolean, nullable=False,default=False)
    general_grade = db.Column(db.Boolean, nullable=False,default=False)
    
    study_type = db.Column(db.Boolean, nullable=False)
    grade = db.Column(db.Boolean, nullable=False)
    origin = db.Column(db.String(255), nullable=False)
    video = db.Column(db.Boolean, nullable=False,default=False)
    
    text = db.Column(db.Text)
    author = db.Column(db.String(2048))
    link = db.Column(db.String(2048), nullable=False)

    thumbnail_link = db.Column(db.String(2048), nullable=True)
    significance = db.Column(db.Float, default=1.0)
    description = db.Column(db.Text)


class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    general_type = db.Column(db.Boolean, nullable=False,default=False)
    general_grade = db.Column(db.Boolean, nullable=False,default=False)
        
    study_type = db.Column(db.Boolean, nullable=False)
    grade = db.Column(db.Boolean, nullable=False)
    origin = db.Column(db.String(255), nullable=False)

    text = db.Column(db.Text)
    author = db.Column(db.String(2048))

    significance = db.Column(db.Float, default=1.0)
    title = db.Column(db.Text, nullable=False)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)
    
    important  = db.Column(db.Boolean, nullable=False, default=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(255), nullable=False)
    male = db.Column(db.Boolean, nullable=False,default=False)
    text = db.Column(db.Text, nullable=True)
    year = db.Column(db.Integer, nullable=False)
    
    username = db.Column(db.String(255), nullable=True)
    group_link = db.Column(db.String(2048), nullable=True)

