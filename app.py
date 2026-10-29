from flask import Flask, render_template, request, redirect, url_for, session, flash
import csv
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'university_erp_secret_key'

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

def read_csv(filename):
    filepath = os.path.join(DATA_DIR, filename)
    data = []
    try:
        with open(filepath, 'r', newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cleaned = {k.strip(): (v.strip() if v else '') for k, v in row.items() if k is not None}
                data.append(cleaned)
    except FileNotFoundError:
        pass
    return data

def write_csv(filename, data, fieldnames):
    filepath = os.path.join(DATA_DIR, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def append_csv(filename, row, fieldnames):
    data = read_csv(filename)
    data.append(row)
    write_csv(filename, data, fieldnames)

def get_next_id(prefix, filename, id_field):
    data = read_csv(filename)
    max_num = 0
    for row in data:
        val = row.get(id_field, '')
        if val.startswith(prefix):
            try:
                num = int(val[len(prefix):])
                if num > max_num:
                    max_num = num
            except ValueError:
                pass
    return f"{prefix}{max_num + 1:03d}"

def get_student_count():
    students = read_csv('students.csv')
    return len(students)

def get_faculty_count():
    faculty = read_csv('faculty.csv')
    return len(faculty)

def get_course_count():
    courses = read_csv('courses.csv')
    return len(courses)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = read_csv('users.csv')
        user = None
        for u in users:
            if u['username'] == username and u['password'] == password:
                user = u
                break
        
        if user:
            session['username'] = username
            session['role'] = user['role']
            session['user_id'] = user.get('user_id', '')
            if user['role'] == 'Admin':
                return redirect(url_for('admin_dashboard'))
            elif user['role'] == 'Faculty':
                return redirect(url_for('faculty_dashboard'))
            elif user['role'] == 'Student':
                return redirect(url_for('student_dashboard'))
            elif user['role'] == 'HOD':
                return redirect(url_for('hod_dashboard'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/admin')
def admin_dashboard():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    student_count = get_student_count()
    faculty_count = get_faculty_count()
    course_count = get_course_count()
    return render_template('admin_dashboard.html', username=session['username'], student_count=student_count, faculty_count=faculty_count, course_count=course_count)

@app.route('/admin/students')
def admin_students():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    students = read_csv('students.csv')
    departments = read_csv('departments.csv')
    return render_template('students.html', students=students, departments=departments)

@app.route('/admin/students/add', methods=['GET', 'POST'])
def add_student():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    if request.method == 'POST':
        student_id = get_next_id('ST', 'students.csv', 'student_id')
        name = request.form['name']
        email = request.form['email']
        department_id = request.form.get('department_id') or request.form.get('course', '')
        semester = request.form['semester']
        
        new_student = {
            'student_id': student_id,
            'name': name,
            'email': email,
            'department_id': department_id,
            'semester': semester
        }
        append_csv('students.csv', new_student, ['student_id', 'name', 'email', 'department_id', 'semester'])
        
        # Also create login account
        username = email.split('@')[0]
        password = '1234'  # Default password
        new_user = {
            'username': username,
            'password': password,
            'role': 'Student',
            'user_id': student_id
        }
        append_csv('users.csv', new_user, ['username', 'password', 'role', 'user_id'])
        
        flash('Student added successfully with login: ' + username + ' / ' + password)
        return redirect(url_for('admin_students'))
    departments = read_csv('departments.csv')
    return render_template('add_student.html', departments=departments)

@app.route('/admin/students/edit/<student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    students = read_csv('students.csv')
    student = None
    for s in students:
        if s['student_id'] == student_id:
            student = s
            break
    
    if request.method == 'POST':
        for s in students:
            if s['student_id'] == student_id:
                s['name'] = request.form['name']
                s['email'] = request.form['email']
                s['department_id'] = request.form.get('department_id') or request.form.get('course', '')
                s['semester'] = request.form['semester']
                break
        write_csv('students.csv', students, ['student_id', 'name', 'email', 'department_id', 'semester'])
        flash('Student updated successfully')
        return redirect(url_for('admin_students'))
    
    departments = read_csv('departments.csv')
    return render_template('edit_student.html', student=student, departments=departments)

@app.route('/admin/students/delete/<student_id>')
def delete_student(student_id):
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    students = read_csv('students.csv')
    students = [s for s in students if s['student_id'] != student_id]
    write_csv('students.csv', students, ['student_id', 'name', 'email', 'department_id', 'semester'])
    flash('Student deleted successfully')
    return redirect(url_for('admin_students'))

@app.route('/admin/faculty')
def admin_faculty():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    faculty = read_csv('faculty.csv')
    departments = read_csv('departments.csv')
    return render_template('faculty.html', faculty=faculty, departments=departments)

@app.route('/admin/faculty/add', methods=['GET', 'POST'])
def add_faculty():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    if request.method == 'POST':
        faculty_id = get_next_id('F', 'faculty.csv', 'faculty_id')
        name = request.form['name']
        email = request.form['email']
        department_id = request.form['department']
        
        new_faculty = {
            'faculty_id': faculty_id,
            'name': name,
            'email': email,
            'department_id': department_id
        }
        append_csv('faculty.csv', new_faculty, ['faculty_id', 'name', 'email', 'department_id'])
        
        # Also create login account
        username = email.split('@')[0]
        password = '1234'  # Default password
        new_user = {
            'username': username,
            'password': password,
            'role': 'Faculty',
            'user_id': faculty_id
        }
        append_csv('users.csv', new_user, ['username', 'password', 'role', 'user_id'])
        
        flash('Faculty added successfully with login: ' + username + ' / ' + password)
        return redirect(url_for('admin_faculty'))
    faculty_list = read_csv('faculty.csv')
    departments = read_csv('departments.csv')
    return render_template('add_faculty.html', departments=departments)

@app.route('/admin/faculty/edit/<faculty_id>', methods=['GET', 'POST'])
def edit_faculty(faculty_id):
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    faculty_list = read_csv('faculty.csv')
    faculty = None
    for f in faculty_list:
        if f['faculty_id'] == faculty_id:
            faculty = f
            break
    
    if request.method == 'POST':
        for f in faculty_list:
            if f['faculty_id'] == faculty_id:
                f['name'] = request.form['name']
                f['email'] = request.form['email']
                f['department_id'] = request.form['department_id']
                break
        write_csv('faculty.csv', faculty_list, ['faculty_id', 'name', 'email', 'department_id'])
        flash('Faculty updated successfully')
        return redirect(url_for('admin_faculty'))
    
    departments = read_csv('departments.csv')
    return render_template('edit_faculty.html', faculty=faculty, departments=departments)

@app.route('/admin/faculty/delete/<faculty_id>')
def delete_faculty(faculty_id):
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    faculty_list = read_csv('faculty.csv')
    faculty_list = [f for f in faculty_list if f['faculty_id'] != faculty_id]
    write_csv('faculty.csv', faculty_list, ['faculty_id', 'name', 'email', 'department_id'])
    flash('Faculty deleted successfully')
    return redirect(url_for('admin_faculty'))

@app.route('/admin/courses')
def admin_courses():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    courses = read_csv('courses.csv')
    faculty_list = read_csv('faculty.csv')
    departments = read_csv('departments.csv')
    return render_template('courses.html', courses=courses, faculty_list=faculty_list, departments=departments)

@app.route('/admin/courses/add', methods=['GET', 'POST'])
def add_course():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    if request.method == 'POST':
        course_id = get_next_id('C', 'courses.csv', 'course_id')
        course_name = request.form['course_name']
        faculty = request.form['faculty']
        semester = request.form['semester']
        
        new_course = {
            'course_id': course_id,
            'course_name': course_name,
            'program': 'AI',  # Default program
            'semester': semester,
            'faculty_id': faculty
        }
        append_csv('courses.csv', new_course, ['course_id', 'course_name', 'program', 'semester', 'faculty_id'])
        flash('Course added successfully')
        return redirect(url_for('admin_courses'))
    faculty_list = read_csv('faculty.csv')
    return render_template('add_course.html', faculty_list=faculty_list)

@app.route('/admin/courses/edit/<course_id>', methods=['GET', 'POST'])
def edit_course(course_id):
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    courses = read_csv('courses.csv')
    course = None
    for c in courses:
        if c['course_id'] == course_id:
            course = c
            break
    
    if request.method == 'POST':
        for c in courses:
            if c['course_id'] == course_id:
                c['course_name'] = request.form['course_name']
                c['faculty_id'] = request.form['faculty']
                c['semester'] = request.form['semester']
                break
        write_csv('courses.csv', courses, ['course_id', 'course_name', 'program', 'semester', 'faculty_id'])
        flash('Course updated successfully')
        return redirect(url_for('admin_courses'))
    
    faculty_list = read_csv('faculty.csv')
    return render_template('edit_course.html', course=course, faculty_list=faculty_list)

@app.route('/admin/courses/delete/<course_id>')
def delete_course(course_id):
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    courses = read_csv('courses.csv')
    courses = [c for c in courses if c['course_id'] != course_id]
    write_csv('courses.csv', courses, ['course_id', 'course_name', 'program', 'semester', 'faculty_id'])
    flash('Course deleted successfully')
    return redirect(url_for('admin_courses'))

@app.route('/admin/student-courses')
def admin_student_courses():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    student_courses = read_csv('student_courses.csv')
    students = read_csv('students.csv')
    courses = read_csv('courses.csv')
    return render_template('student_courses_admin.html', student_courses=student_courses, students=students, courses=courses)

@app.route('/admin/student-courses/add', methods=['GET', 'POST'])
def admin_add_student_course():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        
        student_courses = read_csv('student_courses.csv')
        
        # Check if already exists
        for sc in student_courses:
            if sc['student_id'] == student_id and sc['course_id'] == course_id:
                flash('Student is already enrolled in this course')
                return redirect(url_for('admin_student_courses'))
        
        new_enrollment = {
            'student_id': student_id,
            'course_id': course_id
        }
        append_csv('student_courses.csv', new_enrollment, ['student_id', 'course_id'])
        flash('Student enrolled in course successfully')
        return redirect(url_for('admin_student_courses'))
    
    students = read_csv('students.csv')
    courses = read_csv('courses.csv')
    return render_template('add_student_course.html', students=students, courses=courses)

@app.route('/admin/student-courses/delete/<student_id>/<course_id>')
def admin_delete_student_course(student_id, course_id):
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    student_courses = read_csv('student_courses.csv')
    student_courses = [sc for sc in student_courses if not (sc['student_id'] == student_id and sc['course_id'] == course_id)]
    write_csv('student_courses.csv', student_courses, ['student_id', 'course_id'])
    flash('Student course enrollment deleted successfully')
    return redirect(url_for('admin_student_courses'))

@app.route('/admin/attendance')
def admin_attendance():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    
    # Get filter parameters
    student_id_filter = request.args.get('student_id', '')
    course_id_filter = request.args.get('course_id', '')
    date_filter = request.args.get('date', '')
    
    attendance = read_csv('attendance.csv')
    students = read_csv('students.csv')
    courses = read_csv('courses.csv')
    
    # Apply filters
    if student_id_filter:
        attendance = [a for a in attendance if a['student_id'] == student_id_filter]
    if course_id_filter:
        attendance = [a for a in attendance if a['course_id'] == course_id_filter]
    if date_filter:
        attendance = [a for a in attendance if a['date'] == date_filter]
    
    return render_template('attendance.html', 
                         attendance=attendance, 
                         students=students, 
                         courses=courses,
                         student_id_filter=student_id_filter,
                         course_id_filter=course_id_filter,
                         date_filter=date_filter)

@app.route('/admin/attendance/add', methods=['GET', 'POST'])
def add_attendance():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    
    students = read_csv('students.csv')
    courses = read_csv('courses.csv')
    
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        date = request.form['date']
        status = request.form['status']
        
        # Validation
        if not student_id or not course_id or not date or not status:
            flash('All fields are required')
            return render_template('add_attendance.html', students=students, courses=courses)
        
        if status not in ['Present', 'Absent']:
            flash('Status must be Present or Absent')
            return render_template('add_attendance.html', students=students, courses=courses)
        
        # Check if student exists
        student_exists = any(s['student_id'] == student_id for s in students)
        if not student_exists:
            flash('Invalid student')
            return render_template('add_attendance.html', students=students, courses=courses)
        
        # Check if course exists
        course_exists = any(c['course_id'] == course_id for c in courses)
        if not course_exists:
            flash('Invalid course')
            return render_template('add_attendance.html', students=students, courses=courses)
        
        # Check for duplicate
        attendance = read_csv('attendance.csv')
        for a in attendance:
            if a['student_id'] == student_id and a['course_id'] == course_id and a['date'] == date:
                flash('Attendance already exists for this student, course and date')
                return render_template('add_attendance.html', students=students, courses=courses)
        
        # Add attendance
        new_attendance = {
            'student_id': student_id,
            'course_id': course_id,
            'date': date,
            'status': status
        }
        append_csv('attendance.csv', new_attendance, ['student_id', 'course_id', 'date', 'status'])
        flash('Attendance added successfully')
        return redirect(url_for('admin_attendance'))
    
    return render_template('add_attendance.html', students=students, courses=courses)

@app.route('/admin/attendance/edit/<student_id>/<course_id>/<date>', methods=['GET', 'POST'])
def edit_attendance(student_id, course_id, date):
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    
    attendance = read_csv('attendance.csv')
    students = read_csv('students.csv')
    courses = read_csv('courses.csv')
    
    # Find the attendance record
    record = None
    for a in attendance:
        if a['student_id'] == student_id and a['course_id'] == course_id and a['date'] == date:
            record = a
            break
    
    if not record:
        flash('Attendance record not found')
        return redirect(url_for('admin_attendance'))
    
    if request.method == 'POST':
        status = request.form['status']
        
        if status not in ['Present', 'Absent']:
            flash('Status must be Present or Absent')
        else:
            # Update the record
            for a in attendance:
                if a['student_id'] == student_id and a['course_id'] == course_id and a['date'] == date:
                    a['status'] = status
                    break
            write_csv('attendance.csv', attendance, ['student_id', 'course_id', 'date', 'status'])
            flash('Attendance updated successfully')
            return redirect(url_for('admin_attendance'))
    
    return render_template('edit_attendance.html', record=record, students=students, courses=courses)

@app.route('/admin/attendance/delete/<student_id>/<course_id>/<date>')
def delete_attendance(student_id, course_id, date):
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    
    attendance = read_csv('attendance.csv')
    attendance = [a for a in attendance if not (a['student_id'] == student_id and a['course_id'] == course_id and a['date'] == date)]
    write_csv('attendance.csv', attendance, ['student_id', 'course_id', 'date', 'status'])
    flash('Attendance deleted successfully')
    return redirect(url_for('admin_attendance'))

@app.route('/admin/fees')
def admin_fees():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    fees = read_csv('fees.csv')
    students = read_csv('students.csv')
    return render_template('fees.html', fees=fees, students=students)

@app.route('/admin/fees/update/<student_id>', methods=['GET', 'POST'])
def update_fees(student_id):
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    fees_list = read_csv('fees.csv')
    fee_record = None
    for f in fees_list:
        if f['student_id'] == student_id:
            fee_record = f
            break
    
    if request.method == 'POST':
        paid_fee = int(request.form['paid_fee'])
        for f in fees_list:
            if f['student_id'] == student_id:
                f['paid_fee'] = str(paid_fee)
                f['due_fee'] = str(int(f['total_fee']) - paid_fee)
                f['status'] = 'Paid' if f['due_fee'] == '0' else 'Pending'
                break
        write_csv('fees.csv', fees_list, ['student_id', 'total_fee', 'paid_fee', 'due_fee', 'status'])
        flash('Fee updated successfully')
        return redirect(url_for('admin_fees'))
    
    student = None
    students = read_csv('students.csv')
    for s in students:
        if s['student_id'] == student_id:
            student = s
            break
    
    return render_template('update_fees.html', fee_record=fee_record, student=student)

@app.route('/admin/results')
def admin_results():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    results = read_csv('results.csv')
    students = read_csv('students.csv')
    courses = read_csv('courses.csv')
    return render_template('results.html', results=results, students=students, courses=courses)

@app.route('/admin/results/add', methods=['GET', 'POST'])
def add_result():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        marks = int(request.form['marks'])
        
        if marks >= 90:
            grade = 'A+'
        elif marks >= 80:
            grade = 'A'
        elif marks >= 70:
            grade = 'B+'
        elif marks >= 60:
            grade = 'B'
        elif marks >= 50:
            grade = 'C'
        else:
            grade = 'F'
        
        new_result = {
            'student_id': student_id,
            'course_id': course_id,
            'marks': str(marks),
            'grade': grade
        }
        append_csv('results.csv', new_result, ['student_id', 'course_id', 'marks', 'grade'])
        flash('Result added successfully')
        return redirect(url_for('admin_results'))
    
    students = read_csv('students.csv')
    courses = read_csv('courses.csv')
    return render_template('add_result.html', students=students, courses=courses)

@app.route('/admin/departments')
def admin_departments():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    departments = read_csv('departments.csv')
    faculty_list = read_csv('faculty.csv')
    return render_template('departments.html', departments=departments, faculty_list=faculty_list)

@app.route('/admin/departments/add', methods=['GET', 'POST'])
def admin_add_department():
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    if request.method == 'POST':
        department_id = get_next_id('D', 'departments.csv', 'department_id')
        department_name = request.form['department_name']
        hod_id = request.form.get('hod_id', '')
        
        new_department = {
            'department_id': department_id,
            'department_name': department_name,
            'hod_id': hod_id
        }
        append_csv('departments.csv', new_department, ['department_id', 'department_name', 'hod_id'])
        flash('Department added successfully')
        return redirect(url_for('admin_departments'))
    faculty_list = read_csv('faculty.csv')
    return render_template('add_department.html', faculty_list=faculty_list)

@app.route('/admin/departments/edit/<department_id>', methods=['GET', 'POST'])
def admin_edit_department(department_id):
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    departments = read_csv('departments.csv')
    department = None
    for d in departments:
        if d['department_id'] == department_id:
            department = d
            break
    
    if request.method == 'POST':
        for d in departments:
            if d['department_id'] == department_id:
                d['department_name'] = request.form['department_name']
                d['hod_id'] = request.form.get('hod_id', '')
                break
        write_csv('departments.csv', departments, ['department_id', 'department_name', 'hod_id'])
        flash('Department updated successfully')
        return redirect(url_for('admin_departments'))
    
    faculty_list = read_csv('faculty.csv')
    return render_template('edit_department.html', department=department, faculty_list=faculty_list)

@app.route('/admin/departments/delete/<department_id>')
def admin_delete_department(department_id):
    if session.get('role') != 'Admin':
        return redirect(url_for('login'))
    departments = read_csv('departments.csv')
    departments = [d for d in departments if d['department_id'] != department_id]
    write_csv('departments.csv', departments, ['department_id', 'department_name', 'hod_id'])
    flash('Department deleted successfully')
    return redirect(url_for('admin_departments'))

@app.route('/faculty')
def faculty_dashboard():
    if session.get('role') != 'Faculty':
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    faculty_list = read_csv('faculty.csv')
    faculty_info = None
    for f in faculty_list:
        if f['faculty_id'] == user_id:
            faculty_info = f
            break
    courses = read_csv('courses.csv')
    assigned_courses = [c for c in courses if c['faculty_id'] == faculty_info['faculty_id']] if faculty_info else []
    return render_template('faculty_dashboard.html', faculty=faculty_info, courses=assigned_courses)

@app.route('/faculty/attendance/<course_id>', methods=['GET', 'POST'])
def faculty_attendance(course_id):
    if session.get('role') != 'Faculty':
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    faculty_list = read_csv('faculty.csv')
    faculty_info = None
    for f in faculty_list:
        if f['faculty_id'] == user_id:
            faculty_info = f
            break
    
    courses = read_csv('courses.csv')
    course = None
    for c in courses:
        if c['course_id'] == course_id:
            course = c
            break
    
    # Verify faculty is assigned to this course
    if not faculty_info or not course or course['faculty_id'] != faculty_info['faculty_id']:
        flash('You are not assigned to this course')
        return redirect(url_for('faculty_dashboard'))
    
    # Get students enrolled in this course from student_courses.csv
    student_courses = read_csv('student_courses.csv')
    enrolled_student_ids = [sc['student_id'] for sc in student_courses if sc['course_id'] == course_id]
    students = read_csv('students.csv')
    course_students = [s for s in students if s['student_id'] in enrolled_student_ids]
    
    attendance = read_csv('attendance.csv')
    
    if request.method == 'POST':
        date = request.form['date']
        for student in course_students:
            status = request.form.get(f'status_{student["student_id"]}', 'Absent')
            existing = None
            for a in attendance:
                if a['student_id'] == student['student_id'] and a['course_id'] == course_id and a['date'] == date:
                    existing = a
                    break
            if existing:
                existing['status'] = status
            else:
                new_attendance = {
                    'student_id': student['student_id'],
                    'course_id': course_id,
                    'date': date,
                    'status': status
                }
                attendance.append(new_attendance)
        write_csv('attendance.csv', attendance, ['student_id', 'course_id', 'date', 'status'])
        flash('Attendance marked successfully')
        return redirect(url_for('faculty_attendance', course_id=course_id))
    
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template('faculty_attendance.html', faculty=faculty_info, course=course, students=course_students, attendance=attendance, today=today)

@app.route('/faculty/marks/<course_id>', methods=['GET', 'POST'])
def faculty_marks(course_id):
    if session.get('role') != 'Faculty':
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    faculty_list = read_csv('faculty.csv')
    faculty_info = None
    for f in faculty_list:
        if f['faculty_id'] == user_id:
            faculty_info = f
            break
    
    courses = read_csv('courses.csv')
    course = None
    for c in courses:
        if c['course_id'] == course_id:
            course = c
            break
    
    # Verify faculty is assigned to this course
    if not faculty_info or not course or course['faculty_id'] != faculty_info['faculty_id']:
        flash('You are not assigned to this course')
        return redirect(url_for('faculty_dashboard'))
    
    # Get students enrolled in this course from student_courses.csv
    student_courses = read_csv('student_courses.csv')
    enrolled_student_ids = [sc['student_id'] for sc in student_courses if sc['course_id'] == course_id]
    students = read_csv('students.csv')
    course_students = [s for s in students if s['student_id'] in enrolled_student_ids]
    
    results = read_csv('results.csv')
    
    if request.method == 'POST':
        for student in course_students:
            marks_str = request.form.get(f'marks_{student["student_id"]}', '')
            if marks_str:
                marks = int(marks_str)
                if marks >= 90:
                    grade = 'A+'
                elif marks >= 80:
                    grade = 'A'
                elif marks >= 70:
                    grade = 'B+'
                elif marks >= 60:
                    grade = 'B'
                elif marks >= 50:
                    grade = 'C'
                else:
                    grade = 'F'
                
                existing = None
                for r in results:
                    if r['student_id'] == student['student_id'] and r['course_id'] == course_id:
                        existing = r
                        break
                if existing:
                    existing['marks'] = str(marks)
                    existing['grade'] = grade
                else:
                    new_result = {
                        'student_id': student['student_id'],
                        'course_id': course_id,
                        'marks': str(marks),
                        'grade': grade
                    }
                    results.append(new_result)
        write_csv('results.csv', results, ['student_id', 'course_id', 'marks', 'grade'])
        flash('Marks entered successfully')
        return redirect(url_for('faculty_marks', course_id=course_id))
    
    return render_template('faculty_marks.html', faculty=faculty_info, course=course, students=course_students, results=results)

@app.route('/hod')
def hod_dashboard():
    if session.get('role') != 'HOD':
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    departments = read_csv('departments.csv')
    department = None
    for d in departments:
        if d['hod_id'] == user_id:
            department = d
            break
    faculty_list = read_csv('faculty.csv')
    hod_faculty = None
    for f in faculty_list:
        if f['faculty_id'] == user_id:
            hod_faculty = f
            break
    dept_faculty = [f for f in faculty_list if f['department_id'] == department['department_id']] if department else []
    students = read_csv('students.csv')
    dept_students = [s for s in students if s['department_id'] == department['department_id']] if department else []
    courses = read_csv('courses.csv')
    dept_courses = [c for c in courses if c['department_id'] == department['department_id']] if department else []
    return render_template('hod_dashboard.html', hod=hod_faculty, department=department, faculty=dept_faculty, students=dept_students, courses=dept_courses)

@app.route('/hod/faculty')
def hod_faculty():
    if session.get('role') != 'HOD':
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    departments = read_csv('departments.csv')
    department = None
    for d in departments:
        if d['hod_id'] == user_id:
            department = d
            break
    faculty_list = read_csv('faculty.csv')
    hod_faculty = None
    for f in faculty_list:
        if f['faculty_id'] == user_id:
            hod_faculty = f
            break
    dept_faculty = [f for f in faculty_list if f['department_id'] == department['department_id']] if department else []
    return render_template('hod_faculty.html', hod=hod_faculty, department=department, faculty=dept_faculty)

@app.route('/hod/students')
def hod_students():
    if session.get('role') != 'HOD':
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    departments = read_csv('departments.csv')
    department = None
    for d in departments:
        if d['hod_id'] == user_id:
            department = d
            break
    students = read_csv('students.csv')
    dept_students = [s for s in students if s['department_id'] == department['department_id']] if department else []
    return render_template('hod_students.html', hod=None, department=department, students=dept_students)

@app.route('/hod/courses')
def hod_courses():
    if session.get('role') != 'HOD':
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    departments = read_csv('departments.csv')
    department = None
    for d in departments:
        if d['hod_id'] == user_id:
            department = d
            break
    courses = read_csv('courses.csv')
    dept_courses = [c for c in courses if c['department_id'] == department['department_id']] if department else []
    faculty_list = read_csv('faculty.csv')
    hod_faculty = None
    for f in faculty_list:
        if f['faculty_id'] == user_id:
            hod_faculty = f
            break
    return render_template('hod_courses.html', hod=hod_faculty, department=department, courses=dept_courses, faculty_list=faculty_list)

@app.route('/student')
def student_dashboard():
    if session.get('role') != 'Student':
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    students = read_csv('students.csv')
    departments = read_csv('departments.csv')
    dept_dict = {d['department_id']: d['department_name'] for d in departments}
    student_info = None
    for s in students:
        if s['student_id'] == user_id:
            student_info = s
            break
    if student_info:
        student_info['department_name'] = dept_dict.get(student_info.get('department_id', ''), student_info.get('department_id', ''))
        student_info['course'] = student_info['department_name']
    return render_template('student_dashboard.html', student=student_info)

@app.route('/student/profile')
def student_profile():
    if session.get('role') != 'Student':
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    students = read_csv('students.csv')
    departments = read_csv('departments.csv')
    dept_dict = {d['department_id']: d['department_name'] for d in departments}
    student_info = None
    for s in students:
        if s['student_id'] == user_id:
            student_info = s
            break
    if student_info:
        student_info['department_name'] = dept_dict.get(student_info.get('department_id', ''), student_info.get('department_id', ''))
        student_info['course'] = student_info['department_name']
    return render_template('student_profile.html', student=student_info)

@app.route('/student/attendance')
def student_attendance():
    if session.get('role') != 'Student':
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    students = read_csv('students.csv')
    student_info = None
    for s in students:
        if s['student_id'] == user_id:
            student_info = s
            break
    
    # Get student's enrolled courses from student_courses.csv
    student_courses = read_csv('student_courses.csv')
    enrolled_course_ids = [sc['course_id'] for sc in student_courses if sc['student_id'] == student_info['student_id']] if student_info else []
    
    attendance = read_csv('attendance.csv')
    student_attendance = [a for a in attendance if a['student_id'] == student_info['student_id']] if student_info else []
    
    courses = read_csv('courses.csv')
    course_dict = {c['course_id']: c['course_name'] for c in courses}
    
    for a in student_attendance:
        a['course_name'] = course_dict.get(a['course_id'], a['course_id'])
    
    # Also get all enrolled courses for the summary, even those without attendance records
    enrolled_courses = [c for c in courses if c['course_id'] in enrolled_course_ids]
    
    return render_template('student_attendance.html', student=student_info, attendance=student_attendance, enrolled_courses=enrolled_courses)

@app.route('/student/courses')
def student_courses():
    if session.get('role') != 'Student':
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    students = read_csv('students.csv')
    student_info = None
    for s in students:
        if s['student_id'] == user_id:
            student_info = s
            break
    
    # Get student's enrolled courses from student_courses.csv
    student_courses = read_csv('student_courses.csv')
    enrolled_course_ids = [sc['course_id'] for sc in student_courses if sc['student_id'] == student_info['student_id']] if student_info else []
    
    courses = read_csv('courses.csv')
    faculty_list = read_csv('faculty.csv')
    faculty_dict = {f['faculty_id']: f for f in faculty_list}
    
    # Filter courses to only those the student is enrolled in
    student_enrolled_courses = [c for c in courses if c['course_id'] in enrolled_course_ids]
    
    return render_template('student_courses.html', student=student_info, courses=student_enrolled_courses, faculty_list=faculty_list)

@app.route('/student/fees')
def student_fees():
    if session.get('role') != 'Student':
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    students = read_csv('students.csv')
    student_info = None
    for s in students:
        if s['student_id'] == user_id:
            student_info = s
            break
    
    fees_list = read_csv('fees.csv')
    fee_record = None
    for f in fees_list:
        if f['student_id'] == student_info['student_id']:
            fee_record = f
            break
    
    return render_template('student_fees.html', student=student_info, fee_record=fee_record)

@app.route('/student/results')
def student_results():
    if session.get('role') != 'Student':
        return redirect(url_for('login'))
    user_id = session.get('user_id')
    students = read_csv('students.csv')
    student_info = None
    for s in students:
        if s['student_id'] == user_id:
            student_info = s
            break
    
    # Get student's enrolled courses from student_courses.csv
    student_courses = read_csv('student_courses.csv')
    enrolled_course_ids = [sc['course_id'] for sc in student_courses if sc['student_id'] == student_info['student_id']] if student_info else []
    
    results = read_csv('results.csv')
    student_results = [r for r in results if r['student_id'] == student_info['student_id']] if student_info else []
    
    courses = read_csv('courses.csv')
    course_dict = {c['course_id']: c['course_name'] for c in courses}
    
    for r in student_results:
        r['course_name'] = course_dict.get(r['course_id'], r['course_id'])
    
    # Get all enrolled courses for display, even those without results
    enrolled_courses = [c for c in courses if c['course_id'] in enrolled_course_ids]
    
    return render_template('student_results.html', student=student_info, results=student_results, enrolled_courses=enrolled_courses)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)