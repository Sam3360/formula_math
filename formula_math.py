"""
formula_math.py
A comprehensive Python library for math, finance, geometry, trigonometry, statistics, physics, and original helpers.
"""

import math

# ------------------ Basic Arithmetic ------------------

def add(*args):
    """Returns the sum of any number of numbers"""
    return sum(args)

def sub(a, b):
    """Subtract b from a"""
    return a - b

def multiply(*args):
    """Multiply any number of numbers together"""
    result = 1
    for num in args:
        result *= num
    return result

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def remainder(a, b):
    """Remainder of a divided by b"""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a % b

def sqrt(x):
    """Square root of x"""
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(x)

def solve_expression(expr):
    """
    Solves a math expression given as a string.
    Examples:
    - '2 + 3 * 4'
    - '(5^2 + 3) / 4'
    - 'sqrt(16) + 10'
    """
    expr = expr.replace("^", "**")
    expr = expr.replace("sqrt", "math.sqrt")
    try:
        return eval(expr)
    except Exception as e:
        return f"Error: {e}"

def smart_calc(*args):
    """
    Performs a chain of operations in order:
    Example: smart_calc(10, '+', 5, '*', 2, '-', 4, '/', 2)
    """
    if not args:
        return 0
    expr = ""
    for item in args:
        expr += str(item)
    try:
        return eval(expr)
    except Exception as e:
        return f"Error: {e}"

# ------------------ 2D / 3D Geometry ------------------

def sq_perimeter(side):
    return 4 * side

def rect_area(length, width):
    return length * width

def cube_volume(side):
    return side ** 3

def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

def cone_volume(radius, height):
    return (1/3) * math.pi * radius ** 2 * height

def pyramid_volume(base_length, base_width, height):
    return (1/3) * base_length * base_width * height

def torus_volume(R, r):
    return 2 * (math.pi ** 2) * R * r ** 2

def polygon_area_sides(sides, length):
    angle = math.pi / sides
    return (sides * length**2) / (4 * math.tan(angle))

# ------------------ Finance ------------------

def si(principal, rate, time):
    return principal * rate * time / 100

def ci(principal, rate, time, n=1):
    return principal * ((1 + rate/(100*n))**(n*time) - 1)

def time_to_double(principal, rate):
    return 72 / rate

def emi(principal, rate, time):
    r = rate / (12*100)
    return (principal * r * ((1+r)**time)) / (((1+r)**time)-1)

# ------------------ Algebra ------------------

def solve_quadratic(a, b, c):
    disc = b**2 - 4*a*c
    if disc < 0:
        return None
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)
    return (root1, root2)

def linear_solve_2x2(a1, b1, c1, a2, b2, c2):
    det = a1*b2 - a2*b1
    if det == 0:
        return None
    x = (c1*b2 - c2*b1)/det
    y = (a1*c2 - a2*c1)/det
    return (x, y)

# ------------------ Trigonometry ------------------

def sin_deg(x):
    return math.sin(math.radians(x))

def cos_deg(x):
    return math.cos(math.radians(x))

def heron_area(a, b, c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

# ------------------ Statistics ------------------

def mean(*args):
    return sum(args)/len(args)

def median(*args):
    sorted_args = sorted(args)
    n = len(sorted_args)
    mid = n//2
    if n % 2 == 0:
        return (sorted_args[mid-1] + sorted_args[mid])/2
    else:
        return sorted_args[mid]

def mode(*args):
    from collections import Counter
    count = Counter(args)
    max_count = max(count.values())
    return [k for k,v in count.items() if v == max_count]

def stdev(*args):
    m = mean(*args)
    return math.sqrt(sum((x-m)**2 for x in args)/len(args))

# ------------------ Probability ------------------

def permutations(n, r):
    return math.factorial(n)//math.factorial(n-r)

def combinations(n, r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

# ------------------ Original / Invented Helpers ------------------

def vector_projection(v1, v2):
    dot = sum(a*b for a,b in zip(v1,v2))
    mag_sq = sum(b**2 for b in v2)
    factor = dot/mag_sq
    return tuple(factor*b for b in v2)

def distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def distance_3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def math_trick(x):
    return x**2 + 42

# ------------------ Physics ------------------

def force(mass, acceleration):
    return mass * acceleration

def weight(mass, gravity=9.8):
    return mass * gravity

def work(force, distance, angle_deg=0):
    return force * distance * math.cos(math.radians(angle_deg))

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2

def potential_energy(mass, height, gravity=9.8):
    return mass * gravity * height

def momentum(mass, velocity):
    return mass * velocity

def pressure(force, area):
    return force / area

def density(mass, volume):
    return mass / volume

def velocity(distance, time):
    return distance / time

def acceleration(v_final, v_initial, time):
    return (v_final - v_initial)/time

def grav_force(m1, m2, r):
    G = 6.67430e-11
    return G * m1 * m2 / r**2

def ohms_law(voltage, resistance):
    return voltage / resistance

def electric_power(voltage, current):
    return voltage * current

def coulombs_law(q1, q2, r):
    k = 8.9875517923e9
    return k * q1 * q2 / r**2

