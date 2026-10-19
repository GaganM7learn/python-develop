marks = int(input("Enter your marks:"))
attendance = int(input("Enter your attendance:"))

if marks >= 40:
    if attendance >= 75:
        print("Eligible for exam")
    else :
        print("Attendance too low")
else:
    print("Marks too low")