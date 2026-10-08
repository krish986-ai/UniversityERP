with open('C:/Users/sahil/Desktop/PBL_OS/UniversityERP/app.py', 'r') as f:
    content = f.read()

content = content.replace("course['faculty']", "course['faculty_id']")

with open('C:/Users/sahil/Desktop/PBL_OS/UniversityERP/app.py', 'w') as f:
    f.write(content)
    
print("Updated app.py")