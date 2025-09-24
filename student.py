name = input("Enter the student's name: ")
age = input("Enter the student's age: ")
age4years = int(age) + 4

print(f"Student Name: {name} , Age after 4 years: {age4years}")

gpaMath = float(input("Enter GPA for Math: "))
gpaPhysics = float(input("Enter GPA for Physics: "))
gpaChemistry = float(input("Enter GPA for Chemistry: "))
gpaEnglish = float(input("Enter GPA for English: "))

gpas = [gpaMath, gpaPhysics, gpaChemistry, gpaEnglish]
print(f"GPA for each subject: {gpas}")

averageGpa = sum(gpas) / len(gpas)
print(f"Overal GPA: {averageGpa}")

studentProfile = {
    "name" : name,
    "age" : age,
    "gpas" : gpas,
    "overallGpa" : averageGpa
}

print("Student profile:" , studentProfile)

grades = []
for gpa in gpas:
    if gpa >= 4.0:
        print ("Grade A GPA")
        grades.append("A")
    elif gpa >= 3.0:
        print ("Grade B GPA")
        grades.append("B")
    elif gpa >= 2.0:
        print ("Grade C GPA")
        grades.append("C")
    elif gpa >= 1.0:
        print ("Grade D GPA")
        grades.append("D")
    else:
        print ("Grade F GPA")
        grades.append("F")

print(f"GPA for each subject: {grades}")