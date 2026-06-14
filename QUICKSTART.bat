@echo off
REM Quick Start Guide for Windows - Student Management System

echo ==================================
echo. 🎓 Student Management System
echo. Quick Start Guide
echo ==================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8+
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✅ Python found: %PYTHON_VERSION%
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    echo ✅ Virtual environment created
) else (
    echo ✅ Virtual environment already exists
)

echo.
echo 🔄 Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo 📥 Installing dependencies...
pip install fastapi uvicorn sqlalchemy pydantic -q
echo ✅ Dependencies installed

echo.
echo ==================================
echo. 🚀 BACKEND SETUP COMPLETE
echo ==================================
echo.
echo To start the backend server, run in a new terminal:
echo.   cd backend
echo.   uvicorn main:app --reload
echo.
echo The API will be available at:
echo.   📍 http://localhost:8000
echo.   📊 API Documentation: http://localhost:8000/docs
echo.
echo ==================================
echo. 🎨 FRONTEND SETUP
echo ==================================
echo.
echo To start the frontend, open a new terminal and run:
echo.   cd frontend
echo.   python -m http.server 8001
echo.
echo Then open in your browser:
echo.   🌐 http://localhost:8001/index.html
echo.
echo ==================================
echo. ✨ System is ready to use!
echo ==================================
echo.
pause
