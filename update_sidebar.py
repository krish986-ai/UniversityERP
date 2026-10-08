import glob
import os

templates_dir = 'C:/Users/sahil/Desktop/PBL_OS/UniversityERP/templates'
for f in glob.glob(os.path.join(templates_dir, '*.html')):
    with open(f, 'r') as file:
        content = file.read()
    if 'admin_students' in content and 'admin_faculty' in content:
        old = """<li><a href="{{ url_for('admin_courses') }}">Subject / Course Assignment</a></li>
                    <li><a href="{{ url_for('admin_attendance') }}">Attendance</a></li>"""
        new = """<li><a href="{{ url_for('admin_courses') }}">Subject / Course Assignment</a></li>
                    <li><a href="{{ url_for('admin_student_courses') }}">Student Course Enrollment</a></li>
                    <li><a href="{{ url_for('admin_attendance') }}">Attendance</a></li>"""
        if old in content:
            content = content.replace(old, new)
            with open(f, 'w') as file:
                file.write(content)
            print('Updated:', f)