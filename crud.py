from sqlalchemy.orm import Session

import models
import schemas


def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(
        name=student.name,
        email=student.email,
        phone=student.phone,
        department=student.department,
        year=student.year
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def search_students(db: Session, name: str = None, email: str = None, department: str = None):
    query = db.query(models.Student)
    if name:
        query = query.filter(models.Student.name.ilike(f"%{name}%"))
    if email:
        query = query.filter(models.Student.email.ilike(f"%{email}%"))
    if department:
        query = query.filter(models.Student.department.ilike(f"%{department}%"))
    return query.all()


def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if db_student:
        db_student.name = student.name
        db_student.email = student.email
        db_student.phone = student.phone
        db_student.department = student.department
        db_student.year = student.year

        db.commit()
        db.refresh(db_student)

    return db_student


def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if db_student:
        db.delete(db_student)
        db.commit()

    return db_student


# ==================== COURSES ====================
def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        instructor=course.instructor
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()


def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


def update_course(db: Session, course_id: int, course: schemas.CourseCreate):
    db_course = db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()

    if db_course:
        db_course.name = course.name
        db_course.code = course.code
        db_course.credits = course.credits
        db_course.instructor = course.instructor
        db.commit()
        db.refresh(db_course)

    return db_course


def delete_course(db: Session, course_id: int):
    db_course = db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()

    if db_course:
        db.delete(db_course)
        db.commit()

    return db_course


# ==================== ATTENDANCE ====================
def create_attendance(db: Session, attendance: schemas.AttendanceCreate):
    db_attendance = models.Attendance(
        student_id=attendance.student_id,
        course_id=attendance.course_id,
        date=attendance.date,
        status=attendance.status
    )
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance


def get_attendance(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Attendance).offset(skip).limit(limit).all()


def get_student_attendance(db: Session, student_id: int):
    return db.query(models.Attendance).filter(
        models.Attendance.student_id == student_id
    ).all()


def get_course_attendance(db: Session, course_id: int):
    return db.query(models.Attendance).filter(
        models.Attendance.course_id == course_id
    ).all()


def update_attendance(db: Session, attendance_id: int, attendance: schemas.AttendanceCreate):
    db_attendance = db.query(models.Attendance).filter(
        models.Attendance.id == attendance_id
    ).first()

    if db_attendance:
        db_attendance.student_id = attendance.student_id
        db_attendance.course_id = attendance.course_id
        db_attendance.date = attendance.date
        db_attendance.status = attendance.status
        db.commit()
        db.refresh(db_attendance)

    return db_attendance


def delete_attendance(db: Session, attendance_id: int):
    db_attendance = db.query(models.Attendance).filter(
        models.Attendance.id == attendance_id
    ).first()

    if db_attendance:
        db.delete(db_attendance)
        db.commit()

    return db_attendance


# ==================== GRADES ====================
def create_grade(db: Session, grade: schemas.GradeCreate):
    db_grade = models.Grade(
        student_id=grade.student_id,
        course_id=grade.course_id,
        marks=grade.marks,
        grade=grade.grade
    )
    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)
    return db_grade


def get_grades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Grade).offset(skip).limit(limit).all()


def get_student_grades(db: Session, student_id: int):
    return db.query(models.Grade).filter(
        models.Grade.student_id == student_id
    ).all()


def get_course_grades(db: Session, course_id: int):
    return db.query(models.Grade).filter(
        models.Grade.course_id == course_id
    ).all()


def update_grade(db: Session, grade_id: int, grade: schemas.GradeCreate):
    db_grade = db.query(models.Grade).filter(
        models.Grade.id == grade_id
    ).first()

    if db_grade:
        db_grade.student_id = grade.student_id
        db_grade.course_id = grade.course_id
        db_grade.marks = grade.marks
        db_grade.grade = grade.grade
        db.commit()
        db.refresh(db_grade)

    return db_grade


def delete_grade(db: Session, grade_id: int):
    db_grade = db.query(models.Grade).filter(
        models.Grade.id == grade_id
    ).first()

    if db_grade:
        db.delete(db_grade)
        db.commit()

    return db_grade


# ==================== ENROLLMENTS ====================
def create_enrollment(db: Session, enrollment: schemas.EnrollmentCreate):
    db_enrollment = models.Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        enrollment_date=enrollment.enrollment_date
    )
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment


def get_enrollments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Enrollment).offset(skip).limit(limit).all()


def get_student_enrollments(db: Session, student_id: int):
    return db.query(models.Enrollment).filter(
        models.Enrollment.student_id == student_id
    ).all()


def get_course_enrollments(db: Session, course_id: int):
    return db.query(models.Enrollment).filter(
        models.Enrollment.course_id == course_id
    ).all()


def delete_enrollment(db: Session, enrollment_id: int):
    db_enrollment = db.query(models.Enrollment).filter(
        models.Enrollment.id == enrollment_id
    ).first()

    if db_enrollment:
        db.delete(db_enrollment)
        db.commit()

    return db_enrollment