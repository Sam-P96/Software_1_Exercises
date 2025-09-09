winter, spring, summer, autumn = (12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)

while True:
    x = int(input("Enter the number of a month, and I will tell you what "
                  "saeson it's in. \n >"))
    if x in winter:
        print("Its winter!")
    elif x in spring:
        print("Its spring!")
    elif x in summer:
        print("Its summer!")
    elif x in autumn:
        print("Its autumn")
    else:
        print("That's not a number of a month.")
