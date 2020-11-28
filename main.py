import sympy as sy

x = sy.symbols('x')

intx4 = sy.integrate(x**4,x)
print("The indefinite integral of x^4 is", intx4  )
intsin = sy.integrate(sy.sin(x),x)
print("The indefinite integral of sin(x) is", intsin )
intcos = sy.integrate(-sy.cos(x),x)
print("The indefinite integral of -cos(x) is", intcos  )
