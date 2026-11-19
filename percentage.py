Students = (
    ("Rahul",85),
    ("Raj",76),
    ("Dheeraj",56),
)

print("===== STUDENTS RESULT =====")

for name, Percentage in Students:
    print("Student Name", name)
    print("Percentage", Percentage)

    if Percentage >=60:
        print("first division")
    elif Percentage >=45:
        print("second division")
    elif Percentage >=30:
        print("third division")
    else:
        print("fail")    