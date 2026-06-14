#!/bin/bash
# Quick Start Guide - Student Management System

# This script will help you set up and run the Student Management System

echo "=================================="
echo "🎓 Student Management System"
echo "Quick Start Guide"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.8+"
    exit 1
fi

echo "✅ Python found: $(python --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

echo ""
echo "🔄 Activating virtual environment..."
source venv/Scripts/activate

echo ""
echo "📥 Installing dependencies..."
pip install fastapi uvicorn sqlalchemy pydantic -q
echo "✅ Dependencies installed"

echo ""
echo "=================================="
echo "🚀 BACKEND SETUP COMPLETE"
echo "=================================="
echo ""
echo "To start the backend server, run:"
echo "  cd backend"
echo "  uvicorn main:app --reload"
echo ""
echo "The API will be available at:"
echo "  📍 http://localhost:8000"
echo "  📊 API Documentation: http://localhost:8000/docs"
echo ""
echo "=================================="
echo "🎨 FRONTEND SETUP"
echo "=================================="
echo ""
echo "To start the frontend, open a new terminal and run:"
echo "  cd frontend"
echo "  python -m http.server 8001"
echo ""
echo "Then open in your browser:"
echo "  🌐 http://localhost:8001/index.html"
echo ""
echo "=================================="
echo "✨ System is ready to use!"
echo "=================================="
