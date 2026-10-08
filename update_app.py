with open('C:/Users/sahil/Desktop/PBL_OS/UniversityERP/app.py', 'r') as f:
    content = f.read()

# Replace s['course'] with s['program'] in student routes
content = content.replace("s['course']", "s['program']")
content = content.replace("student_info['course']", "student_info['program']")

with open('C:/Users/sahil/Desktop/PBL_OS/UniversityERP/app.py', 'w') as f:
    f.write(content)
    
print("Updated app.py")