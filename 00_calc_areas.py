#use function
#invoke functons
#ask user what he wants to solve
#Ronny Coulson
#calc areas from the menu, applying while learning
import math
def menu():
    print("Select Option you want to solve")
    print("[1] Rectangle")
    print("[2] Square")
    print("[3] Circle")
    print("[4] Exit")


def calcRectangle():
    print("You se;ect to solve a Rectangle")
    lenght = float(input("Enter lenght: "))
    width = float(input("Enter width: "))
    area = lenght * width
    print(f"The area of the rectangle is {area}cm^2 ")
    return lenght, width

def calcCircle():
    print("You se;ect to solve a Circle")
    radious = float(input("Enter radious: "))
    area = math.pi * pow(radious,2)
    print(f"The area of the circle is {round(area, 2)}cm^2")
    return radious

def calcSquare():
    print("You select to solve a square")
    sides = int(input("Enter sides lenght: "))
    area = sides * 4
    print(f"The area of the square is {area}cm ")
    return sides


def main():
    option = True
    RECTANGLE = 1
    SQUARE = 2
    CIRCLE = 3
    EXIT = 4
    while option:
        menu()
        option = int(input("Choose option -> "))

        if option == RECTANGLE:
            lenght, rectangle = calcRectangle()
        elif option == SQUARE:
            side = calcSquare()
        elif option == CIRCLE:
            radious = calcCircle()
        elif option == EXIT:
            print("Exit Program")
            option = False
        else:
            print("Invalid. Try again")

main()






