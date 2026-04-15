from faker import Faker
import random
from db import SessionLocal
from models import Group, Student, Teacher, Subject, Grade

fake = Faker()
session = SessionLocal()

# --- GROUPS ---
groups = []
for i in range(3):
    group = Group(name=f"Group-{i+1}")
    session.add(group)
    groups.append(group)

session.commit()

# --- TEACHERS ---
teachers = []
for _ in range(random.randint(3, 5)):
    teacher = Teacher(name=fake.name())
    session.add(teacher)
    teachers.append(teacher)

session.commit()

# --- SUBJECTS ---
subjects = []
for i in range(random.randint(5, 8)):
    subject = Subject(
        name=f"Subject-{i+1}",
        teacher=random.choice(teachers)
    )
    session.add(subject)
    subjects.append(subject)

session.commit()

# --- STUDENTS ---
students = []
for _ in range(random.randint(30, 50)):
    student = Student(
        name=fake.name(),
        group=random.choice(groups)
    )
    session.add(student)
    students.append(student)

session.commit()

# --- GRADES ---
for student in students:
    for _ in range(random.randint(10, 20)):
        grade = Grade(
            student=student,
            subject=random.choice(subjects),
            grade=random.randint(1, 12)
        )
        session.add(grade)

session.commit()

session.close()

print("Database seeded successfully!")