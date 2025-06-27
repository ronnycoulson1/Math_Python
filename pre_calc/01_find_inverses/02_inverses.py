import sympy
#find iverse algebraically use a function
#function to solve -> f(x) = x^2-4x. x >= 2
#Ronny coulson
#practicing math and coding to learn and familiarize

import sympy
import cmath
def calcEquation():

    print("Equation to be solved: f(x) = x^2 - 4x, >=2")
    x,y = sympy.symbols('x y') # create 2 varaibles x and y for function
    f = x**2 -4*x #equation
    print(f)
    equation = sympy.Eq(y,f)
    print(f"Step 1: Equation values: {equation} ", " -> y = x^2-4x")

    swapped = sympy.Eq(x, f.subs(x, y))
    print(f"Step 2: Swapped f for x: {swapped} ",  " ->  x = y^2-4x")

    solution = sympy.solve(swapped,y)
    #takes equation x = y^2 - 4y
    #rewrite it in quadratic from y^2 - 4y - x = 0
    #recognize patter ay^2 + by + c = 0
    print(f"Step 3: Solutions  for x: {solution}")
calcEquation()



