// Backend API Helper Functions

const API_BASE_URL = 'http://localhost:8000/students';

// Create a new student
async function createStudent(studentData) {
    try {
        const response = await fetch(`${API_BASE_URL}/students/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(studentData)
        });
        return await response.json();
    } catch (error) {
        console.error('Error creating student:', error);
    }
}

// Get all students
async function getStudents() {
    try {
        const response = await fetch(`${API_BASE_URL}/students/`);
        return await response.json();
    } catch (error) {
        console.error('Error fetching students:', error);
    }
}

// Get a specific student
async function getStudent(studentId) {
    try {
        const response = await fetch(`${API_BASE_URL}/students/${studentId}`);
        return await response.json();
    } catch (error) {
        console.error('Error fetching student:', error);
    }
}

// Update a student
async function updateStudent(studentId, studentData) {
    try {
        const response = await fetch(`${API_BASE_URL}/students/${studentId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(studentData)
        });
        return await response.json();
    } catch (error) {
        console.error('Error updating student:', error);
    }
}

// Delete a student
async function deleteStudent(studentId) {
    try {
        const response = await fetch(`${API_BASE_URL}/students/${studentId}`, {
            method: 'DELETE'
        });
        return await response.json();
    } catch (error) {
        console.error('Error deleting student:', error);
    }
}