from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from routers import students, courses, attendance, enrollments, grades, reports

app = FastAPI(
    title="Student Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(students.router)
app.include_router(courses.router)
app.include_router(attendance.router)
app.include_router(enrollments.router)
app.include_router(grades.router)
app.include_router(reports.router)

@app.get("/")
def home():
    return {
        "message": "Student Management System API",
        "endpoints": {
            "students": "/students",
            "courses": "/courses",
            "enrollments": "/enrollments",
            "attendance": "/attendance",
            "grades": "/grades",
            "reports": "/reports"
        }
    }
