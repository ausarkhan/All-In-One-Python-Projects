# Student Management System

A complete GUI-based Student Management System built with Python.

## Features
- Add new students with automated roll number assignment
- Update student information (address, date of birth)
- Delete student records
- Search by roll number or name
- Secure login interface for administrators only

## Technologies Used
- Python
- Tkinter (GUI)
- Pandas, Numpy (data storage and logic)

## Usage
1. Run `main.py`.
2. Login with username: `admin`, password: `password` (default, can be changed in code).
3. Use the GUI to manage student records.

## Data Storage
Student data is stored in `students.csv` in the same directory.

## Requirements
- Python 3.x
- pandas
- numpy

Install dependencies:
```bash
pip install pandas numpy
```

## Customization
- Change admin credentials in `main.py` (`ADMIN_USER`, `ADMIN_PASS`).

## License
MIT
