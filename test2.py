import sympy as sym


eq1 = "x1*1+y*3-10"
eq2 = "x2-y-5"

solution = sym.solve([eq1, eq2])
print(solution)