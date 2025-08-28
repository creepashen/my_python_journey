grades = {'nawaf': 90, 'fahad': 85, 'sara': 97, 'ali': 70}

high_grade_ = None
best_name_ = None

for name, grade in grades.items():
   
    if high_grade_ is None or grade >= high_grade_:
        
        high_grade_ = grade
        name_ = name

print("Best grade in class for: ",name_, high_grade_)

low_grade = None
worse_name = None

for name_f , grade_f in grades.items():
    
    if low_grade is None or grade_f <= low_grade:
       
        low_grade = grade_f
        worse_name = name_f
print("Less degree in the class for: ", worse_name, low_grade)