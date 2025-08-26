# I used while True cus I think that its better that its repeatable
# but ofcourse I'd use break if the program should end after printing the results

while True:
    a = float(input("""Give me a year, and I will let you know whether or not it is a leap year. 
Enter Year: """))
    if a % 100 == 0 and a % 400 == 0:
        print("This is a leap year")
        print("=" * 100 + "\n")
    elif a % 100 == 0:
        print("This is not a leap year")
        print("=" * 100 + "\n")
    elif a % 4 == 0:
        print("This is a leap year")
        print("=" * 100 + "\n")
    else:
        print("This is not a leap year")
        print("=" * 100 + "\n")