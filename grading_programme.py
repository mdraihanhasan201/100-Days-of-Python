student_score={"rayhan":92,
               "tawfique":80,
               "rafi":60,
               "limon":50,
               "siam":40
}

print(student_score)
student_grade={}

for student in student_score:
    score=student_score[student]

    if score>90:
        student_grade[student]="outstanding"
    elif score>80:
        student_grade[student]="great"
    elif score > 70:
        student_grade[student] = "good"
    elif score > 60:
        student_grade[student] = "average"
    else:
        student_grade[student] = "fail"

print(student_grade)

