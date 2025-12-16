#[Nyari Mushaikwa]
#[T level Year 1]
#RobustProgram.py

try:
    age = int(input("Enter age:"))
    if 0 <= age <= 120:
        if age >= 18:
            print("Adult")
        else:
            print("Minor")
    else:
        print("Error: Age must be 0-120")
except ValueError:
    print("Error: Please enter a number")
