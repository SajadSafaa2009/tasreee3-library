from app import db
from app.models.models import Tip , Source , Article , Student
from sqlalchemy import or_

def get_sources(origin, grade, study_type):
    return Source.query.filter(
        Source.origin == origin,
        Source.video == False,
        or_(Source.general_grade == True, Source.grade == grade),
        or_(Source.general_type == True, Source.study_type == study_type)
    ).order_by(Source.significance.desc(), Source.id.asc()).all()


def get_videos(origin, grade, study_type):
    return Source.query.filter(
        Source.origin == origin,
        Source.video == True,
        or_(Source.general_grade == True, Source.grade == grade),
        or_(Source.general_type == True, Source.study_type == study_type)
    ).order_by(Source.significance.desc(), Source.id.asc()).all()


from sqlalchemy import or_

def get_tips(origin, grade, study_type):
    subject_origins = {"physics", "math", "biology", "chemistry"}
    post_subject_origins = {
        "english", "arabic", "french", "religion",
        "math2", "physics2", "chemistry2", "biology2"
    }

    allowed_origins = [origin]

    if origin in subject_origins:
        allowed_origins.append("subjects")
        allowed_origins.append("subjects+iq")
    elif origin == "iq":
        allowed_origins.append("subjects+iq")
    elif origin in post_subject_origins:
        allowed_origins.append("post-subjects")

    return Tip.query.filter(
        Tip.origin.in_(allowed_origins),
        or_(Tip.general_grade == True, Tip.grade == grade),
        or_(Tip.general_type == True, Tip.study_type == study_type)
    ).order_by(Tip.significance.desc(), Tip.id.asc()).all()


def get_articles():
    return Article.query.order_by(Article.date.desc(), Article.id.asc()).all()

def add_source(study_type, grade, origin, text, author, link, significance, description,general_grade,general_type):
    new_source = Source(
        study_type=study_type,
        grade=grade,
        origin=origin,
        text=text,
        author=author,
        link=link,
        significance=significance,
        description=description,
        general_grade=general_grade,
        general_type=general_type,
        video=False
    )
    db.session.add(new_source)
    db.session.commit()

def add_video(study_type, grade, origin, text, author, link, significance, description,general_grade,general_type):
    new_video = Source(
        study_type=study_type,
        grade=grade,
        origin=origin,
        text=text,
        author=author,
        link=link,
        significance=significance,
        description=description,
        general_grade=general_grade,
        general_type=general_type,
        video=True
    )
    db.session.add(new_video)
    db.session.commit()

def add_tip(study_type, grade, origin, title, author, significance, text,general_grade,general_type):
    new_tip = Tip(
        study_type=study_type,
        grade=grade,
        origin=origin,
        title=title,
        text=text,
        author=author,
        significance=significance,
        general_grade=general_grade,
        general_type=general_type,

    )
    db.session.add(new_tip)
    db.session.commit()

def add_article(title,text,date,important):
    new_article = Article(
        title=title,
        text=text,
        date=date,
        important=important
    )
    db.session.add(new_article)
    db.session.commit()

def add_student(name, text, year, username,group_link):
    new_student = Student(
        name=name,
        text=text,
        year=year,
        username=username,
        group_link=group_link
    )
    db.session.add(new_student)
    db.session.commit()