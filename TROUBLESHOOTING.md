# 🔧 Troubleshooting Guide - Courses, Attendance, Grades

## ✅ What Was Fixed

1. **Added Missing CRUD Functions** - The backend `crud.py` was missing all functions for:
   - Courses (create, read, update, delete)
   - Attendance (create, read, update, delete, filter by student/course)
   - Grades (create, read, update, delete, filter by student/course)
   - Enrollments (create, read, delete, filter by student/course)

2. **Improved Error Handling** - JavaScript files now show better error messages when:
   - Backend is not running
   - Network errors occur
   - API returns errors

## 🚀 How to Test

### Step 1: Start Backend Server
```bash
cd backend
uvicorn main:app --reload
```

Expected output:
```
INFO:     Started server process
INFO:     Application startup complete
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Step 2: Start Frontend
Open new terminal:
```bash
cd frontend
python -m http.server 8001
```

Then open: `http://localhost:8001/index.html`

### Step 3: Test Each Feature

#### Test Courses
1. Go to "📖 Courses" page
2. Fill in form:
   - Course Name: "Mathematics 101"
   - Course Code: "MATH101"
   - Credits: 3
   - Instructor: "Dr. Smith"
3. Click "Add Course"
4. Should see: ✅ Course Added Successfully!
5. Course appears in table below

#### Test Attendance
1. Go to "✓ Attendance" page
2. First, ensure you have students and courses (add some from their pages)
3. Fill in form:
   - Student ID: 1 (or valid student ID)
   - Course ID: 1 (or valid course ID)
   - Date: 2026-06-14
   - Status: "Present"
4. Click "Mark Attendance"
5. Should see: ✅ Attendance Marked!
6. Record appears in table with color-coded status

#### Test Grades
1. Go to "📊 Grades" page
2. First, ensure you have students and courses
3. Fill in form:
   - Student ID: 1
   - Course ID: 1
   - Marks: 85.5
   - Grade: "A"
4. Click "Add Grade"
5. Should see: ✅ Grade Added!
6. Grade appears in table

## 🐛 Common Issues & Solutions

### Issue: "Failed to load courses/attendance/grades"
**Cause:** Backend server is not running
**Solution:**
1. Make sure `uvicorn main:app --reload` is running in backend folder
2. Check terminal for any error messages
3. Verify you're on `http://localhost:8000/docs` - Swagger UI should load

### Issue: "Network error"
**Cause:** CORS issue or backend not accessible
**Solution:**
1. Check backend terminal for errors
2. Ensure CORS middleware is enabled in `main.py`
3. Try accessing `http://localhost:8000/docs` directly in browser

### Issue: "Error: Unable to add course"
**Cause:** Course code might already exist (unique constraint)
**Solution:**
- Use different course code
- Try: "CS301", "PHY201", "BIO401" etc.

### Issue: Empty tables even after adding data
**Cause:** Page not refreshing data after addition
**Solution:**
1. Hard refresh browser: `Ctrl+F5` or `Cmd+Shift+R`
2. Close browser dev tools: Press `F12` to toggle
3. Check browser console for JavaScript errors

### Issue: "Failed to mark attendance" or "Failed to add grade"
**Cause:** Invalid student ID or course ID
**Solution:**
1. First add students via "👥 Students" page
2. First add courses via "📖 Courses" page
3. Use valid IDs (start with 1)
4. Check that students and courses exist before adding attendance/grades

## 🔍 How to Debug

### Check Browser Console
1. Press `F12` to open Developer Tools
2. Click "Console" tab
3. Look for any error messages in red
4. These errors help identify issues

### Check Backend Terminal
1. Look at the terminal running `uvicorn main:app --reload`
2. Any API errors will be printed there
3. Look for status codes like `404`, `500`, `422`

### Test API Directly
Open browser and try:
- `http://localhost:8000/courses/` - Should return empty list `[]`
- `http://localhost:8000/attendance/` - Should return empty list `[]`
- `http://localhost:8000/grades/` - Should return empty list `[]`
- `http://localhost:8000/docs` - Should show Swagger UI with all endpoints

## ✨ Expected Behavior

### Adding Data
- ✅ Form clears after successful add
- ✅ Alert shows success message
- ✅ Table updates immediately with new row
- ✅ ID auto-increments

### Loading Data
- ✅ Tables load when page opens
- ✅ Empty message shows if no data
- ✅ Error message shows if backend fails

### Color Coding (Attendance)
- 🟢 Green = Present
- 🔴 Red = Absent
- 🟡 Yellow = Late

## 📊 Sample Test Data

### Add Students First
```
Name: John Doe, Email: john@example.com, Phone: 1234567890, Department: CS, Year: 1
Name: Jane Smith, Email: jane@example.com, Phone: 0987654321, Department: CS, Year: 2
```

### Add Courses
```
Name: Python Programming, Code: CS101, Credits: 3, Instructor: Prof. Johnson
Name: Web Development, Code: CS201, Credits: 3, Instructor: Prof. Williams
```

### Then Add Attendance & Grades
```
Mark attendance for Student 1, Course 1, Status: Present
Add grade: Student 1, Course 1, Marks: 85, Grade: A
```

## 📞 Still Having Issues?

1. Check backend `crud.py` - should have 30+ functions
2. Verify all routers in `main.py` are imported
3. Check `database.py` - models should be created on startup
4. Clear browser cache: `Ctrl+Shift+Delete`
5. Restart both backend and frontend servers
6. Check terminal for Python errors

---

**System should now work! 🎉**
