# University ERP Platform

A beginner-level University ERP (Enterprise Resource Planning) platform built for college/student projects. This project demonstrates web development, file handling, database concepts, and basic Operating System concepts using simple technologies.

## Project Purpose

This project is designed as a learning tool for beginner-level computer science/engineering students to understand:
- Web application development with Flask
- File-based data storage using CSV files
- Role-based access control (Admin, Faculty, Student)
- CRUD operations (Create, Read, Update, Delete)
- Basic Operating System concepts in a practical context

## Features

### Admin Module
- Student Management: Add, View, Edit, Delete students
- Faculty Management: Add, View, Edit, Delete faculty
- Course Management: Add, View, Edit, Delete courses
- Attendance Report: View attendance records for all students
- Fees Management: View and update student fee status
- Results Management: Add and view student marks/grades

### Faculty Module
- Dashboard showing assigned courses
- Mark Attendance for assigned courses
- Enter Marks for assigned courses

### Student Module
- View Profile
- View Attendance with summary percentage
- View Courses
- View Fees status
- View Results/Grades

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Backend**: Python 3, Flask
- **Database**: CSV Files (using Python's built-in `csv` module)
- **No external dependencies**: No MySQL, MongoDB, Firebase, PostgreSQL, Docker, React, Node.js, TypeScript, or cloud services

## Installation

1. **Prerequisites**: Python 3.7 or higher installed on your laptop

2. **Clone/Download** the project to your local machine

3. **Install Flask**:
   ```bash
   pip install flask
   ```

4. **Navigate to project directory**:
   ```bash
   cd UniversityERP
   ```

## How to Run

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000
   ```

3. Login with demo credentials:

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| Faculty | sharma | 1234 |
| Faculty | kumar | 1234 |
| Faculty | singh | 1234 |
| Faculty | patel | 1234 |
| Student | rahul | 1234 |
| Student | aman | 1234 |
| Student | priya | 1234 |
| Student | neha | 1234 |

## Folder Structure

```
UniversityERP/
│
├── app.py                 # Main Flask application
│
├── data/                  # CSV Database Files
│   ├── users.csv          # Login credentials and roles
│   ├── students.csv       # Student information
│   ├── faculty.csv        # Faculty information
│   ├── courses.csv        # Course information
│   ├── attendance.csv     # Attendance records
│   ├── fees.csv           # Fee records
│   └── results.csv        # Marks and grades
│
├── templates/             # HTML Templates
│   ├── login.html
│   ├── admin_dashboard.html
│   ├── students.html
│   ├── add_student.html
│   ├── edit_student.html
│   ├── faculty.html
│   ├── add_faculty.html
│   ├── edit_faculty.html
│   ├── courses.html
│   ├── add_course.html
│   ├── edit_course.html
│   ├── attendance.html
│   ├── fees.html
│   ├── update_fees.html
│   ├── results.html
│   ├── add_result.html
│   ├── faculty_dashboard.html
│   ├── faculty_attendance.html
│   ├── faculty_marks.html
│   ├── student_dashboard.html
│   ├── student_profile.html
│   ├── student_attendance.html
│   ├── student_courses.html
│   ├── student_fees.html
│   └── student_results.html
│
├── static/                # Static Assets
│   ├── style.css          # Styling
│   └── script.js          # Client-side JavaScript
│
└── README.md              # This file
```

## Database/CSV Structure

### users.csv
```csv
username,password,role,user_id
admin,admin123,Admin,A001
sharma,1234,Faculty,F001
kumar,1234,Faculty,F002
singh,1234,Faculty,F003
patel,1234,Faculty,F004
rahul,1234,Student,ST001
aman,1234,Student,ST002
priya,1234,Student,ST003
neha,1234,Student,ST004
```

### students.csv
```csv
student_id,name,email,course,semester
ST001,Rahul,rahul@gmail.com,AI,3
ST002,Aman,aman@gmail.com,CSE,3
ST003,Priya,priya@gmail.com,AI,3
ST004,Neha,neha@gmail.com,CSE,3
```

### faculty.csv
```csv
faculty_id,name,email,department
F001,Dr. Sharma,sharma@gmail.com,AI
F002,Mr. Kumar,kumar@gmail.com,CSE
F003,Dr. Singh,singh@gmail.com,AI
F004,Ms. Patel,patel@gmail.com,CSE
```

### courses.csv
```csv
course_id,course_name,faculty,semester
C001,Operating System,F001,3
C002,Machine Learning,F003,3
C003,Computer Networks,F001,3
C004,Database Management,F001,3
```

### attendance.csv
```csv
student_id,course_id,date,status
ST001,C001,2026-10-08,Present
ST002,C001,2026-10-08,Absent
ST003,C002,2026-10-08,Present
ST004,C002,2026-10-08,Present
ST001,C001,2026-10-07,Present
ST002,C001,2026-10-07,Present
ST003,C002,2026-10-07,Absent
ST004,C002,2026-10-07,Present
```

### fees.csv
```csv
student_id,total_fee,paid_fee,due_fee,status
ST001,100000,95000,5000,Pending
ST002,100000,100000,0,Paid
ST003,100000,50000,50000,Pending
ST004,100000,100000,0,Paid
```

### results.csv
```csv
student_id,course_id,marks,grade
ST001,C001,90,A+
ST002,C001,85,A
ST003,C002,92,A+
ST004,C002,75,B
ST001,C003,88,A
ST002,C003,82,A-
ST003,C004,90,A+
ST003,C001,85,A
```

## Project Flow

```
START
  ↓
Open ERP Application (python app.py)
  ↓
Login Page
  ↓
Check Username & Password in users.csv
  ↓
Valid?
 ┌──────────────┐
 NO             YES
 ↓               ↓
Login Error    Check Role
                 ↓
       ┌─────────┼─────────┐
       ↓         ↓         ↓
     Admin     Faculty   Student
       ↓         ↓         ↓
   Dashboard  Dashboard Dashboard
       ↓         ↓         ↓
 Manage Data Attendance   View Data
       ↓         ↓         ↓
     CSV File ←────────────┘
       ↓
Update / Read Data
       ↓
Display Result
       ↓
Logout
       ↓
END
```

## Data Flow Diagram (DFD)

### Level 0 (Context Diagram)
```
[Admin] ──────────────┐
                      ▼
[Faculty] ──► [University ERP] ──► [CSV Files]
                      ▲
[Student] ────────────┘
```

### Level 1 (Main Processes)
```
[Login] ──► [Authenticate] ──► [Route by Role]

[Admin Dashboard] ──► [Students CRUD] ──► [students.csv]
                   ├──► [Faculty CRUD]  ──► [faculty.csv]
                   ├──► [Courses CRUD]  ──► [courses.csv]
                   ├──► [Attendance]    ──► [attendance.csv]
                   ├──► [Fees]          ──► [fees.csv]
                   └──► [Results]       ──► [results.csv]

[Faculty Dashboard] ──► [Mark Attendance] ──► [attendance.csv]
                     ├──► [Enter Marks]      ──► [results.csv]

[Student Dashboard] ──► [View Profile]  ──► [students.csv]
                     ├──► [View Attendance] ──► [attendance.csv]
                     ├──► [View Courses]      ──► [courses.csv]
                     ├──► [View Fees]         ──► [fees.csv]
                     └──► [View Results]      ──► [results.csv]
```

## ER-Style Data Relationship Diagram (CSV-Based)

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│   users     │       │  students   │       │  faculty    │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ username PK │       │ student_id  │       │ faculty_id  │
│ password    │       │ name        │       │ name        │
│ role        │       │ email       │       │ email       │
└─────────────┘       │ course      │       │ department  │
                      │ semester    │       └──────┬──────┘
                      └──────┬──────┘              │
                             │                     │
              ┌──────────────┼──────────────┐      │
              ▼              ▼              ▼      ▼
       ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
       │ attendance  │ │    fees     │ │   courses   │
       ├─────────────┤ ├─────────────┤ ├─────────────┤
       │ student_id  │ │ student_id  │ │ course_id   │
       │ course_id   │ │ total_fee   │ │ course_name │
       │ date        │ │ paid_fee    │ │ faculty FK  │
       │ status      │ │ due_fee     │ │ semester    │
       └──────┬──────┘ │ status      │ └──────┬──────┘
              │        └─────────────┘        │
              │              ▲                │
              ▼              │                ▼
       ┌─────────────┐      │         ┌─────────────┐
       │  results    │      │         │  faculty    │
       ├─────────────┤      │         │  (dept)     │
       │ student_id  │      └─────────│  matches    │
       │ course_id   │                │  student    │
       │ marks       │                │  course     │
       │ grade       │                └─────────────┘
       └─────────────┘
```

**Relationships:**
- `users` → `students` (1:1) via username/email prefix
- `users` → `faculty` (1:1) via username/email prefix
- `students` → `attendance` (1:M) via student_id
- `students` → `fees` (1:1) via student_id
- `students` → `results` (1:M) via student_id
- `courses` → `attendance` (1:M) via course_id
- `courses` → `results` (1:M) via course_id
- `faculty` → `courses` (1:M) via faculty_id
- `students.course` matches `faculty.department` for course enrollment

## Module Descriptions

### 1. Login Module (`/login`)
- Handles authentication for all three roles
- Reads `users.csv` to verify credentials
- Creates session with username and role
- Redirects to appropriate dashboard based on role

### 2. Admin Module (`/admin/*`)
- **Dashboard** (`/admin`): Overview with statistics
- **Students** (`/admin/students`): Full CRUD operations
- **Faculty** (`/admin/faculty`): Full CRUD operations
- **Courses** (`/admin/courses`): Full CRUD operations
- **Attendance** (`/admin/attendance`): Read-only report view
- **Fees** (`/admin/fees`, `/admin/fees/update/<id>`): View and update
- **Results** (`/admin/results`, `/admin/results/add`): View and add

### 3. Faculty Module (`/faculty/*`)
- **Dashboard** (`/faculty`): Shows assigned courses
- **Attendance** (`/faculty/attendance/<course_id>`): Mark Present/Absent
- **Marks** (`/faculty/marks/<course_id>`): Enter numerical marks (auto-calculates grade)

### 4. Student Module (`/student/*`)
- **Dashboard** (`/student`): Welcome page with quick links
- **Profile** (`/student/profile`): View personal information
- **Attendance** (`/student/attendance`): View records with percentage summary
- **Courses** (`/student/courses`): View enrolled courses
- **Fees** (`/student/fees`): View fee status
- **Results** (`/student/results`): View marks and grades

## Operating System Concepts Used

### 1. Process Management
**Concept**: When we run `python app.py`, the operating system creates a process for the Flask application.

**Explanation**: The OS assigns a Process ID (PID) to the running Python/Flask application, allocates memory, and manages its execution. The process runs independently and the OS scheduler gives it CPU time.

**In Project**: 
- The Flask development server runs as a single process
- Each HTTP request is handled within this process
- The OS manages process lifecycle (start, run, terminate)

### 2. File Management
**Concept**: The ERP stores all data in CSV files managed by the operating system's file system.

**Explanation**: The OS provides a file system (NTFS on Windows, ext4 on Linux) that organizes data into files and directories. It handles file creation, deletion, reading, writing, and permissions.

**In Project**:
```
University ERP Application
         ↓
Python File Handling (csv module)
         ↓
CSV Files (users.csv, students.csv, etc.)
         ↓
Operating System File System
```

### 3. File Read/Write Operations
**Concept**: When the application reads or updates data, it performs file I/O operations managed by the OS.

**Explanation**: 
- **Read Operation**: Application → OS → File System → Disk → Data returned to Application
- **Write Operation**: Application → OS → File System → Disk (data persisted)

**In Project**:
```python
# Read example (in app.py)
with open('data/students.csv', 'r') as f:
    reader = csv.DictReader(f)
    students = list(reader)

# Write example (in app.py)
with open('data/students.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)
```

### 4. Memory Management
**Concept**: While the ERP is running, the OS loads the program code and data into RAM.

**Explanation**: The OS allocates virtual memory for the Python process, loads the Flask framework, application code, and CSV data into physical RAM. When memory is low, the OS may swap to disk.

**In Project**:
- Flask application code loaded in memory
- CSV data read into Python data structures (lists/dicts) in RAM
- Session data stored in memory (Flask sessions)
- OS handles memory allocation and garbage collection

### 5. CPU Management / Process Scheduling
**Concept**: The OS provides CPU time to the running Flask/Python process.

**Explanation**: The OS scheduler (typically Round Robin or similar) allocates CPU time slices to the Flask process. When a request comes in, the process executes, then yields CPU to other processes.

**In Project**:
- Single-threaded Flask development server
- Handles one request at a time (sequential)
- OS scheduler manages CPU time between Flask and other system processes
- No custom CPU scheduling implemented (beginner project)

### 6. File Permissions (Basic)
**Concept**: The OS controls who can read/write the CSV files.

**Explanation**: File permissions (read, write, execute) are managed by the OS. On Windows, this is handled by ACLs; on Linux by rwx permissions.

**In Project**:
- Application runs with user's permissions
- CSV files created with default user permissions
- Read/Write access controlled by OS

## Testing

### Manual Testing Checklist

#### Admin Tests
- [ ] Login as admin (admin/admin123)
- [ ] View admin dashboard with statistics
- [ ] Add new student → verify in list and CSV
- [ ] Edit existing student → verify changes
- [ ] Delete student → verify removal
- [ ] Add new faculty → verify in list and CSV
- [ ] Edit faculty → verify changes
- [ ] Delete faculty → verify removal
- [ ] Add new course → verify in list and CSV
- [ ] Edit course → verify changes
- [ ] Delete course → verify removal
- [ ] View attendance report → check data display
- [ ] View fees → check all records
- [ ] Update fee for student → verify status change
- [ ] View results → check all records
- [ ] Add new result → verify grade calculation

#### Faculty Tests
- [ ] Login as faculty (sharma/1234)
- [ ] View faculty dashboard with assigned courses
- [ ] Mark attendance for course C001
- [ ] Verify attendance saved in CSV
- [ ] Enter marks for course C001
- [ ] Verify marks and grades saved in CSV

#### Student Tests
- [ ] Login as student (rahul/1234)
- [ ] View student dashboard
- [ ] View profile → check all fields
- [ ] View attendance → check records and percentage
- [ ] View courses → check enrolled courses
- [ ] View fees → check status
- [ ] View results → check marks and grades

#### Cross-Role Tests
- [ ] Admin cannot access faculty/student URLs
- [ ] Faculty cannot access admin/student URLs
- [ ] Student cannot access admin/faculty URLs
- [ ] Logout clears session → redirects to login

### Automated Test Results
All endpoints tested and returning HTTP 200:
- Admin: 6/6 endpoints working
- Faculty: 3/3 endpoints working
- Student: 6/6 endpoints working
- CRUD Operations: All working (Create, Read, Update, Delete)

## Limitations

This is a **beginner-level college project** with the following limitations:

1. **CSV Database**: Not suitable for large-scale university databases (no indexing, no concurrent access control, no transactions)
2. **No Multi-User Online Access**: Single-user offline application
3. **Basic Authentication**: Plain text passwords, no encryption/hashing, no JWT/OAuth
4. **No Cloud Storage**: All data stored locally on laptop
5. **No Real-Time Synchronization**: No WebSockets or live updates
6. **Single-Threaded**: Flask development server handles one request at a time
7. **No Advanced Security**: No CSRF protection, no SQL injection prevention (not needed for CSV), no rate limiting
8. **Basic UI**: No complex animations, charts, or advanced frontend features
9. **No Email Notifications**: No SMTP integration
10. **No Mobile Application**: Web-only interface

## Future Scope

Simple enhancements that could be added later:

1. **Database Upgrade**: Replace CSV with SQLite/MySQL/PostgreSQL
2. **Better Authentication**: Password hashing (bcrypt), session management, JWT tokens
3. **Online Deployment**: Deploy to cloud (Heroku, AWS, Azure, etc.)
4. **Email Notifications**: Fee reminders, attendance alerts, result notifications
5. **Mobile Application**: React Native or Flutter app
6. **Advanced Reporting**: PDF reports, charts, analytics dashboard
7. **Better Security**: HTTPS, CSRF tokens, input validation, rate limiting
8. **Multi-Tenancy**: Support multiple universities
9. **API Layer**: REST API for third-party integrations
10. **Audit Logging**: Track all changes for accountability

## Conclusion

This University ERP Platform demonstrates a complete, functional web application built with beginner-friendly technologies. It successfully implements:

- **Three-role access control** (Admin, Faculty, Student)
- **Full CRUD operations** on all entities
- **CSV-based persistence** using Python's standard library
- **Clean MVC-like architecture** with Flask
- **Responsive UI** with vanilla HTML/CSS/JS
- **Operating System concepts** explained in practical context

The project is ideal for:
- College project submissions
- Learning Flask web development
- Understanding file-based data storage
- Demonstrating OS concepts in application context
- Portfolio demonstration for beginners

---

**Project Status**: Complete and Tested  
**Difficulty Level**: Beginner  
**Lines of Code**: ~600 (Python) + ~2000 (HTML/CSS/JS)  
**Dependencies**: Flask only (standard library for everything else)