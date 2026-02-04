#!/bin/bash

echo "==============================================="
echo "CareerIQ - AI Career Guidance - Startup Script"
echo "==============================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "Python found: $(python3 --version)"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created!"
fi

echo ""
echo "Activating virtual environment..."
source venv/bin/activate

echo ""
echo "Installing/Updating dependencies..."
pip install -r requirements.txt

echo ""
echo "==============================================="
echo "Starting CareerIQ..."
echo "==============================================="
echo ""
echo "The application will be available at:"
echo "http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 run.py
