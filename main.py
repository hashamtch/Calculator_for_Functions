
print("*******AREA of the Calculator*******")
print(""""Press 1 to get a the area of square
Press 2 to get the area of rectangle
Press 3 to get the area of the circle
Press 4 to get the area of the triangle""")

choice = int(input("Enter a number between 1 to 4"))
if choice == 1:
    side = int(input("Enter the side of the number"))
    area = side * side
    print("The area of the Square is = " , area)
elif choice == 2:
    length = int(input("Enter a number"))
    width = int(input("Enter a number"))
    area = length * width
    print("The area of rectangle is = " , area)
elif choice == 3:
    radius = int(input("Enter a number"))
    area = ((22/7)*(radius*radius))
    print("The are of Radius is =" , area)
elif choice == 4:
    base = float(input("Enter any number"))
    height = float(input("Enter any number"))
    area = (1/2)*(base*height)
    print("The area of Triangle is =", area)
else:
    print("Invalid")
    print("Please")