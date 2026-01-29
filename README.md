# formula_math
🧮 Formula Math (formula_math)

Formula Math is a comprehensive Python library designed to bring essential math, physics, finance, and geometry formulas directly to your fingertips. Whether you are a student, teacher, or developer, formula_math eliminates the need to look up constants or derive complex equations — just import and solve.

🚀 Key Features

Finance: Quick calculations for interest and savings.

Geometry: Full support for 2D areas/perimeters and 3D volumes/surface areas.

Physics: Basic kinematics, dynamics, and energy calculations.

Algebra: Solve quadratics and find means instantly.

Trigonometry: Intuitive degree-based calculations.

Combinatorics: Easy access to factorials, permutations, and combinations.

📦 Installation

Install the package via pip:

pip install formula_math


🛠 Usage

Simply import the library and use the fm alias for a faster workflow:

import formula_math as fm

# Example: Calculate the area of a circle with radius 7
result = fm.circle_area(7)
print(result) # Output: 153.938


📚 API Reference

1️⃣ Finance Formulas

Function

Parameters

Description

Example

si(p, r, t)

Principal, Rate(%), Time(yrs)

Simple Interest

fm.si(1000, 5, 1) → 50.0

ci(p, r, t)

Principal, Rate(%), Time(yrs)

Compound Interest

fm.ci(1000, 5, 2) → 102.5

2️⃣ 2D Geometry

Function

Parameters

Description

Example

sq_perimeter(s)

side

Perimeter of a square

fm.sq_perimeter(5) → 20

sq_area(s)

side

Area of a square

fm.sq_area(5) → 25

rect_perimeter(l, b)

length, breadth

Perimeter of a rectangle

fm.rect_perimeter(4, 5) → 18

rect_area(l, b)

length, breadth

Area of a rectangle

fm.rect_area(4, 5) → 20

circle_area(r)

radius

Area of a circle

fm.circle_area(7) → 153.938

circle_circumference(r)

radius

Circumference of a circle

fm.circle_circumference(7) → 43.982

tri_area_base_height(b, h)

base, height

Triangle area (standard)

fm.tri_area_base_height(4, 5) → 10.0

tri_area_sides(a, b, c)

sides a, b, c

Triangle area (Heron’s)

fm.tri_area_sides(3,4,5) → 6.0

tri_perimeter(a, b, c)

sides a, b, c

Perimeter of triangle

fm.tri_perimeter(3,4,5) → 12

3️⃣ 3D Geometry

Function

Parameters

Description

Example

cube_volume(s)

side

Volume of cube

fm.cube_volume(3) → 27

cube_surface_area(s)

side

Total surface area of cube

fm.cube_surface_area(3) → 54

cuboid_volume(l, b, h)

length, breadth, height

Volume of cuboid

fm.cuboid_volume(2,3,4) → 24

cuboid_surface_area(l,b,h)

length, breadth, height

Surface area of cuboid

fm.cuboid_surface_area(2,3,4) → 52

sphere_volume(r)

radius

Volume of sphere

fm.sphere_volume(3) → 113.097

sphere_surface_area(r)

radius

Surface area of sphere

fm.sphere_surface_area(3) → 113.097

cylinder_volume(r, h)

radius, height

Volume of cylinder

fm.cylinder_volume(3,5) → 141.372

cylinder_surface_area(r,h)

radius, height

Surface area of cylinder

fm.cylinder_surface_area(3,5) → 150.796

cone_volume(r, h)

radius, height

Volume of cone

fm.cone_volume(3,5) → 47.123

cone_surface_area(r, l)

radius, slant height

Surface area of cone

fm.cone_surface_area(3,5) → 75.398

hemisphere_volume(r)

radius

Volume of hemisphere

fm.hemisphere_volume(3) → 56.548

hemisphere_surface_area(r)

radius

Total surface area

fm.hemisphere_surface_area(3) → 84.823

4️⃣ Algebra

Function

Parameters

Description

Example

quad_roots(a, b, c)

coefficients ($ax^2+bx+c=0$)

Real or Complex roots

fm.quad_roots(1,-3,2) → (2.0,1.0)

arithmetic_mean(*args)

numbers

Average (Mean)

fm.arithmetic_mean(2,4,6) → 4.0

geometric_mean(*args)

numbers

Geometric Mean

fm.geometric_mean(2,8) → 4.0

5️⃣ Trigonometry (Degrees)

Function

Parameters

Description

Example

sin_deg(x)

angle in degrees

Sine of angle

fm.sin_deg(30) → 0.5

cos_deg(x)

angle in degrees

Cosine of angle

fm.cos_deg(60) → 0.5

tan_deg(x)

angle in degrees

Tangent of angle

fm.tan_deg(45) → 1.0

cosec_deg(x)

angle in degrees

Cosecant of angle

fm.cosec_deg(30) → 2.0

sec_deg(x)

angle in degrees

Secant of angle

fm.sec_deg(60) → 2.0

cot_deg(x)

angle in degrees

Cotangent of angle

fm.cot_deg(45) → 1.0

6️⃣ Physics (Basic)

Function

Parameters

Description

Example

speed(d, t)

distance, time

Speed calculation

fm.speed(100,5) → 20.0

distance(s, t)

speed, time

Distance calculation

fm.distance(20,5) → 100

time(d, s)

distance, speed

Time calculation

fm.time(100,20) → 5.0

force(m, a)

mass, acceleration

Force ($F = ma$)

fm.force(10,9.8) → 98.0

weight(m, g=9.8)

mass, gravity

Weight

fm.weight(10) → 98.0

kinetic_energy(m, v)

mass, velocity

Kinetic Energy ($\frac{1}{2}mv^2$)

fm.kinetic_energy(10,5) → 125.0

potential_energy(m,h,g=9.8)

mass, height, gravity

Potential Energy ($mgh$)

fm.potential_energy(10,5) → 490.0

work(f, d)

force, distance

Work Done ($W = Fd$)

fm.work(10,5) → 50

pressure(f, a)

force, area

Pressure ($P = F/A$)

fm.pressure(100,5) → 20.0

7️⃣ Miscellaneous

Function

Parameters

Description

Example

factorial(x)

integer

Factorial ($n!$)

fm.factorial(5) → 120

fibonacci(n)

number of terms

Fibonacci sequence

fm.fibonacci(7) → [0,1,1,2,3,5,8]

nCr(n, r)

total, selected

Combinations

fm.nCr(5,2) → 10

nPr(n, r)

total, selected

Permutations

fm.nPr(5,2) → 20

📝 Notes

Trigonometry: All trig functions use degrees for ease of use in educational contexts.

Units: Ensure all inputs for geometry and physics are in consistent units (e.g., all meters or all centimeters).

Target Audience: This library is optimized for K-12 students and introductory college-level calculations.

🤝 Contributing

Contributions make the open-source community an amazing place!

Fork the project.

Create your feature branch (git checkout -b feature/NewFormula).

Commit your changes (git commit -m 'Add some NewFormula').

Push to the branch (git push origin feature/NewFormula).

Open a Pull Request.

📄 License

Distributed under the MIT License. See LICENSE.txt for more information.
