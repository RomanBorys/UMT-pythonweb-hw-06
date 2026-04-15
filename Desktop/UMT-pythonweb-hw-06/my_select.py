from db import SessionLocal
from models import Student, Group, Teacher, Subject, Grade
from sqlalchemy import func

session = SessionLocal()

def select_1():
    return session.query(
        Student.name,
        func.round(func.avg(Grade.grade), 2).label("avg_grade")
    ).join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()


def select_2(subject_name):
    return session.query(
        Student.name,
        func.avg(Grade.grade).label("avg_grade")
    ).join(Grade).join(Subject).filter(Subject.name == subject_name)\
     .group_by(Student.id)\
     .order_by(func.avg(Grade.grade).desc()).first()


def select_3(subject_name):
    return session.query(
        Group.name,
        func.avg(Grade.grade)
    ).select_from(Group)\
     .join(Student)\
     .join(Grade)\
     .join(Subject)\
     .filter(Subject.name == subject_name)\
     .group_by(Group.id).all()


def select_4():
    return session.query(func.avg(Grade.grade)).scalar()

def select_5(teacher_name):
    return session.query(Subject.name)\
        .join(Teacher)\
        .filter(Teacher.name == teacher_name).all()


def select_6(group_name):
    return session.query(Student.name)\
        .join(Group)\
        .filter(Group.name == group_name).all()


def select_7(group_name, subject_name):
    return session.query(Student.name, Grade.grade)\
        .join(Group)\
        .join(Grade)\
        .join(Subject)\
        .filter(Group.name == group_name, Subject.name == subject_name)\
        .all()


def select_8(teacher_name):
    return session.query(func.avg(Grade.grade))\
        .join(Subject)\
        .join(Teacher)\
        .filter(Teacher.name == teacher_name)\
        .scalar()


def select_9(student_name):
    return session.query(Subject.name)\
        .join(Grade)\
        .join(Student)\
        .filter(Student.name == student_name)\
        .distinct().all()


def select_10(student_name, teacher_name):
    return session.query(Subject.name)\
        .join(Grade)\
        .join(Student)\
        .join(Teacher)\
        .filter(Student.name == student_name, Teacher.name == teacher_name)\
        .distinct().all()


session.close()