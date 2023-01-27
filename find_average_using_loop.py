student_nam=input("input student number").split()

for n in range(0, len(student_nam)):
    student_nam[n]=int(student_nam[n])
print(student_nam)
total_num=sum(student_nam)
student_average=total_num/len(student_nam)
print(student_average)
