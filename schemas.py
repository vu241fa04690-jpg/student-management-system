from pydantic import BaseModel
from datetime import date

class StudentCreate(BaseModel):
    name: str
    email: str
    phone: str
    department: str
    year: int

class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True


class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    instructor: str

class CourseResponse(CourseCreate):
    id: int

    class Config:
        from_attributes = True


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int
    enrollment_date: date

class EnrollmentResponse(EnrollmentCreate):
    id: int

    class Config:
        from_attributes = True


class AttendanceCreate(BaseModel):
    student_id: int
    course_id: int
    date: date
    status: str

class AttendanceResponse(AttendanceCreate):
    id: int

    class Config:
        from_attributes = True


class GradeCreate(BaseModel):
    student_id: int
    course_id: int
    marks: float
    grade: str

class GradeResponse(GradeCreate):
    id: int

    class Config:
        from_attributes = True