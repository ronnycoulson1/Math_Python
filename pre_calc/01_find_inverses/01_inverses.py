#find iverse algebraically use a function
#function to solve -> f(x) = 4-5x

import sympy

def calcEquation():

    print("Funtion: f(x)=4-5x")
    x, y = sympy.symbols("x y")
    f = 4 - 5 * x

    equation = sympy.Eq(y, f)
    swapped = sympy.Eq(x, f.subs(x, y))
    solution = sympy.solve(swapped, y)

    if solution:
        inverseEquation = sympy.together(solution[0])
        print(f"The inverse is y={inverseEquation}")
    else:
        print("Mo inverse")

calcEquation()
