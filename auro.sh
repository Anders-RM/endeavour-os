#!/bin/bash

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Python is not installed. Installing Python..."
    sudo pacman -Sy --noconfirm python
    echo "Python has been installed."
else
    echo "Python is already installed."
fi

# Execute the Python script
echo "Starting Python script..."
python setup.py
