#[Nyari Mushaikwa]
#[T level Year 1]
#RobustProgram.py

status = False

while(not status):
    try:
        age = int(input("Enter age:"))
        if 0 > age and age < 120:
            if age >= 18:
                print("Valid age")
                status = True
            else:
                print("You are under 18")
                status = True
    
    except ValueError:
        print("Error: Please enter a valid age")
