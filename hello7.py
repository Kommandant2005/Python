a=input("Enter Weekday: ")
if a in ("Sunday","sunday","SUNDAY"):
    print("It is a holiday")
elif a in ("Saturday","saturday","SATURDAY"):
    print("It is weekend")
elif a in ("monday","tuesday","wednesday","thursday","friday"):
    print("It is a working day")
else:
    print("Enter correct day")
