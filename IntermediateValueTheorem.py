"""
The IntermediateValueTheorem program applies the calculus Intermediate Value Theorem Principle 
in Python.

file: IntermediateValueTheorem.py
author: Goutam Kanamarlapudi
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify

"""
intermediate_value_theorem function that utilizes the the calculus theorem of IVT to calculate 
the Intermediate Value Theorem Principle.

@param f function that is used for IVT
@param a first x-value start point
@param b second x-value end point
@param y-value to look for in the interval
@return True if IVT holds, False otherwise
"""
def intermediate_value_theorem(f, a, b, N):
    # Evaluate the function at the endpoints
    f_a = f(a)
    f_b = f(b)

    # Check if the target value N is between f(a) and f(b)
    if (f_a <= N <= f_b) or (f_b <= N <= f_a):
        # Precision of approximation
        tolerance = 1e-6
        while abs(b - a) > tolerance:
            c = (a + b) / 2
            f_c = f(c)

            if abs(f_c - N) < tolerance:
                return True, f"There exists a c = {c:.6f} such that f(c) ≈ {N}."

            if f_c < N:
                a = c
            else:
                b = c

        return False, "Could not find an exact value, but IVT suggests it should exist."
    else:
        return False, f"IVT does not hold: N = {N} is not between f(a) = {f_a} and f(b) = {f_b}."

"""
create_function function that converts a string polynomial function into a Python function

@param user_input string polynomial function
@return function that evaluates the polynomial function
"""
def create_function(user_input):
    """Convert a string polynomial function into a Python function."""
    x = symbols('x')
    expr = sympify(user_input)  # Convert string to sympy expression
    func = lambda x_val: float(expr.subs(x, x_val))  # Evaluate for numerical inputs
    return func

"""
plot_function function that plots the polynomial function with the interval highlighted

@param f function that is used for IVT
@param a first x-value start point
@param b second x-value end point
"""
def plot_function(f, a, b):
    """Plot the polynomial function with the interval [a, b] highlighted."""
    x_vals = np.linspace(a-1, b+1, 400)
    y_vals = [f(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label="f(x)", color='blue')
    plt.axhline(0, color='black',linewidth=1)  # x-axis
    plt.axvline(a, color='red', linestyle='--', label=f"a = {a}")
    plt.axvline(b, color='green', linestyle='--', label=f"b = {b}")
    plt.title(f"Graph of the function with interval [{a}, {b}]")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

"""
main function that runs the program and prints to the output
"""
def main():
    print("Advanced IVT Calculator")

    # Take user input for the function
    user_function = input("Enter a polynomial function of x (e.g., x**3 - 6*x**2 + 11*x - 6): ")

    # Create the function from user input
    f = create_function(user_function)

    # Take user input for the interval [a, b]
    a = float(input("Enter the starting point a: "))
    b = float(input("Enter the ending point b: "))

    # Take user input for the target value N (default is 0)
    N = float(input("Enter the target value N (default is 0): ") or 0)

    # Check if the IVT holds
    result, message = intermediate_value_theorem(f, a, b, N)

    # Output the result
    print(message)

    # Plot the function (optional but helpful for visualization)
    plot_function(f, a, b)

main()
