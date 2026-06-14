# 📚 EduDash - Student Management System

A complete, attractive student management portal with modern UI design and comprehensive features.

## 🎯 Features Implemented

### 1. **Students Management** (Full CRUD)
- Create new students with details (name, email, phone, department, year)
- View all students in a beautiful table layout
- Search students by name, email, or department
- Delete student records
- Real-time student count on dashboard

### 2. **Courses Management** (Full CRUD)
- Add new courses (name, code, credits, instructor)
- View all courses
- Manage course information
- Real-time course count on dashboard

### 3. **Attendance Tracking**
- Mark attendance for students per course
- Track status (Present, Absent, Late)
- View attendance history with date and status
- Color-coded status display (Green for Present, Red for Absent, Yellow for Late)

### 4. **Grades & Marks**
- Record student grades for each course
- Track marks and letter grades
- Full CRUD operations for grades
- View grades by student or course

### 5. **Student Enrollment**
- Link students to courses
- Manage enrollments
- Track enrollment dates

### 6. **Reports & Analytics**
- **Student Grade Report**: View total marks and average marks for a student
- **Student Attendance Report**: View attendance percentage, present, absent, and late counts
- **Course Summary Report**: View total students, graded count, and average marks

### 7. **Search & Filter**
- Advanced student search by name, email, department
- Pagination support for large datasets

## 🏗️ Architecture

### Backend
- **Framework**: FastAPI (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **API**: RESTful endpoints for all entities
- **Middleware**: CORS enabled for cross-origin requests
- **Validation**: Pydantic schemas for request/response validation

### Frontend
- **HTML5/CSS3/Vanilla JavaScript** (No frameworks for simplicity)
- **Modern UI Design** with gradient backgrounds, cards, and smooth animations
- **Responsive Layout** - Sidebar navigation on desktop, mobile-friendly
- **Real-time API Integration** - All pages fetch data from backend

## 📁 Project Structure

```
Student management system/
├── backend/
│   ├── main.py                 # FastAPI application entry point
│   ├── database.py             # SQLAlchemy database configuration
│   ├── models.py               # SQLAlchemy ORM models
│   ├── schemas.py              # Pydantic validation schemas
│   ├── crud.py                 # Database CRUD operations
│   ├── routers/
│   │   ├── students.py         # Student API endpoints
│   │   ├── courses.py          # Course API endpoints
│   │   ├── attendance.py       # Attendance API endpoints
│   │   ├── enrollments.py      # Enrollment API endpoints
│   │   ├── grades.py           # Grades API endpoints
│   │   └── reports.py          # Reports API endpoints
│   └── students.db             # SQLite database file
│
├── frontend/
│   ├── index.html              # Dashboard (home page)
│   ├── students.html           # Students management page
│   ├── courses.html            # Courses management page
│   ├── attendance.html         # Attendance tracking page
│   ├── grades.html             # Grades management page
│   ├── reports.html            # Reports & analytics page
│   ├── css/
│   │   └── style.css           # Modern CSS styling
│   └── js/
│       ├── app.js              # Core JavaScript
│       ├── students.js         # Student functionality
│       ├── courses.js          # Course functionality
│       ├── attendance.js       # Attendance functionality
│       ├── grades.js           # Grades functionality
│       └── reports.js          # Reports functionality
│
└── venv/                        # Python virtual environment
```

## 🚀 Setup & Run Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### 1. Backend Setup

1. **Create and activate virtual environment**:
   ```bash
   cd g:\Student management system
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
   ```

3. **Run the backend server**:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
   
   The API will be available at: `http://localhost:8000`
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### 2. Frontend Setup

1. **Open frontend in browser**:
   ```bash
   cd g:\Student management system\frontend
   ```
   
2. **Option A - Using Python's built-in server**:
   ```bash
   python -m http.server 8001
   ```
   Then open: `http://localhost:8001/index.html`

3. **Option B - Using Live Server (VS Code)**:
   - Install "Live Server" extension in VS Code
   - Right-click on `index.html` → "Open with Live Server"

## 📊 Database Models

### Student
- `id`: Primary Key
- `name`: String
- `email`: Unique String
- `phone`: String
- `department`: String
- `year`: Integer
- Relationships: enrollments, attendance, grades

### Course
- `id`: Primary Key
- `name`: String
- `code`: Unique String
- `credits`: Integer
- `instructor`: String
- Relationships: enrollments, attendance, grades

### Enrollment
- `id`: Primary Key
- `student_id`: Foreign Key (Student)
- `course_id`: Foreign Key (Course)
- `enrollment_date`: Date

### Attendance
- `id`: Primary Key
- `student_id`: Foreign Key (Student)
- `course_id`: Foreign Key (Course)
- `date`: Date
- `status`: String (Present/Absent/Late)

### Grade
- `id`: Primary Key
- `student_id`: Foreign Key (Student)
- `course_id`: Foreign Key (Course)
- `marks`: Float (0-100)
- `grade`: String (A, B, C, etc)

## 🎨 UI Features

- **Sidebar Navigation**: Fixed left sidebar with emoji-based navigation
- **Dashboard**: Overview cards showing total students, courses, attendance rate, average grade
- **Modern Color Scheme**: Purple gradient backgrounds with professional color palette
- **Card-based Layouts**: Clean, organized card components for content
- **Responsive Tables**: Data displayed in styled, hover-responsive tables
- **Form Grids**: Multi-column responsive forms for data entry
- **Status Badges**: Color-coded status indicators for attendance
- **Smooth Animations**: Hover effects and transitions throughout

## 🔧 API Endpoints

### Students
- `POST /students/` - Create student
- `GET /students/` - List all students (with pagination)
- `GET /students/{id}` - Get specific student
- `GET /students/search/all` - Search students
- `PUT /students/{id}` - Update student
- `DELETE /students/{id}` - Delete student

### Courses
- `POST /courses/` - Create course
- `GET /courses/` - List all courses
- `GET /courses/{id}` - Get specific course
- `PUT /courses/{id}` - Update course
- `DELETE /courses/{id}` - Delete course

### Attendance
- `POST /attendance/` - Mark attendance
- `GET /attendance/` - List all attendance
- `GET /attendance/student/{id}` - Get student attendance
- `GET /attendance/course/{id}` - Get course attendance
- `PUT /attendance/{id}` - Update attendance
- `DELETE /attendance/{id}` - Delete attendance

### Enrollments
- `POST /enrollments/` - Create enrollment
- `GET /enrollments/` - List all enrollments
- `GET /enrollments/student/{id}` - Get student enrollments
- `GET /enrollments/course/{id}` - Get course enrollments
- `DELETE /enrollments/{id}` - Delete enrollment

### Grades
- `POST /grades/` - Add grade
- `GET /grades/` - List all grades
- `GET /grades/student/{id}` - Get student grades
- `GET /grades/course/{id}` - Get course grades
- `PUT /grades/{id}` - Update grade
- `DELETE /grades/{id}` - Delete grade

### Reports
- `GET /reports/student/{id}/grades` - Student grade report
- `GET /reports/student/{id}/attendance` - Student attendance report
- `GET /reports/course/{id}/summary` - Course summary report

## 💡 Usage Examples

### Adding a Student
1. Go to "Students" page
2. Fill in the "Add New Student" form with name, email, phone, department, year
3. Click "Add Student"
4. Student appears in the table immediately

### Marking Attendance
1. Go to "Attendance" page
2. Enter Student ID, Course ID, Date, and Status
3. Click "Mark Attendance"
4. Record appears in the attendance table

### Viewing Reports
1. Go to "Reports" page
2. Select report type (Student Grade, Attendance, or Course Summary)
3. Enter the student/course ID
4. Click "Generate" to view the report

## 🔐 Security Notes

- CORS is enabled for all origins (for development)
- For production, restrict `allow_origins` to specific domains
- Add authentication/authorization as needed
- Use environment variables for sensitive configuration

## 🐛 Troubleshooting

### Backend won't start
- Ensure Python 3.8+ is installed
- Verify virtual environment is activated
- Check that port 8000 is not in use

### Frontend can't connect to API
- Ensure backend is running on `localhost:8000`
- Check browser console for error messages
- Verify CORS is enabled in backend

### Database errors
- Delete `students.db` file to reset database
- Ensure backend creates database on first run
- Check SQLAlchemy models are valid

## 📝 Next Steps (Optional Enhancements)

- Add user authentication and authorization
- Implement data validation and error handling
- Add email notifications
- Create admin dashboard with advanced analytics
- Add file upload for bulk student import
- Implement backup and restore functionality
- Add dark mode toggle
- Implement role-based access control
- Add audit logging for all operations
- Create mobile app version

## 👨‍💻 Technologies Used

- **Backend**: FastAPI, SQLAlchemy, Pydantic, Python 3.8+
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite
- **Development Server**: Uvicorn

## 📄 License

This project is open source and available for educational purposes.

---

**Enjoy your attractive Student Management Portal! 🎓**
