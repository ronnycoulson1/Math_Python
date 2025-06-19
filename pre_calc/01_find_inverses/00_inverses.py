#find inverses algebraically
#Ronny Coulson
#function 1: f = 2 * x +3
#6/19/2025

import sympy #math library

#sympy.symbols() function from sympy that create variables
#this function ask to give me variables named x y to be used for algebra
#return 2 objs that can be used for mathematical expressions 2*x*3*y
x, y = sympy.symbols("x y")
f = 2 * x + 3

#representation y = f(x) or y = 2x+ 3
#sympy.Eq(lhs, rhs) meaning lhs = rhs
equation = sympy.Eq(y, f) #creates an equation

#f = 2x+3 -> y=2x+3 (first swap)
# x=2*y+3 (second swap)
#f,subs(x,y) replace all the x in the equation for y
swapped = sympy.Eq(x,f.subs(x,y)) #solve x's for y's

#solve for y
solution = sympy.solve(swapped, y)

if solution:
    inverse_equation = sympy.together(solution[0]) #simplyfy result
    print(f"The inverse of the equation is: {inverse_equation}")
else:
    print("No inverse")






move 00_inverses.py ..\00_calc_areas\Math_Python\pre_calc\01_find_inverses\
