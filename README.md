🧮 Formula Math (formula_math)

Formula Math is a comprehensive Python library designed to make math, physics, finance, and geometry formulas instantly accessible in one place. It’s perfect for students, teachers, hobbyists, or developers who want to save time and avoid remembering formulas.

🎯 Target Audience & Benefits

Who is this for?

Students: Simplify homework and verify complex calculations across math and physics.

Educators: Use it as a teaching tool to demonstrate formula applications in Python.

Developers: A lightweight utility for apps requiring quick geometry or finance logic without heavy dependencies.

Why use formula_math?

Save Time: No need to look up constants (like $\pi$ or $g$) or derive formulas from scratch.

Accuracy: Built-in logic handles edge cases like complex roots in quadratics.

Readability: Clean, intuitive function names make your code easier for others to understand.

🚀 Key Features

Finance: Quick calculations for simple and compound interest.

Geometry: Full support for 2D (Area/Perimeter) and 3D (Volume/Surface Area).

Physics: Kinematics, dynamics, energy, and pressure.

Algebra: Solve quadratics and calculate means.

Trigonometry: Intuitive degree-based functions.

Miscellaneous: Factorials, Fibonacci, and Combinatorics.

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

si(p, r, t) – p=Principal, r=Rate %, t=Time (yrs). Calculates Simple Interest.

Example: fm.si(1000, 5, 1) → 50.0

ci(p, r, t) – p=Principal, r=Rate %, t=Time (yrs). Calculates Compound Interest.

Example: fm.ci(1000, 5, 2) → 102.5

2️⃣ 2D Geometry

sq_perimeter(x) – x=side. Perimeter of a square.

Example: fm.sq_perimeter(5) → 20

sq_area(x) – x=side. Area of a square.

Example: fm.sq_area(5) → 25

rect_perimeter(l, b) – l=length, b=breadth. Perimeter of a rectangle.

Example: fm.rect_perimeter(4, 5) → 18

rect_area(l, b) – l=length, b=breadth. Area of a rectangle.

Example: fm.rect_area(4, 5) → 20

circle_area(r) – r=radius. Area of a circle.

Example: fm.circle_area(7) → 153.938

circle_circumference(r) – r=radius. Circumference of a circle.

Example: fm.circle_circumference(7) → 43.982

tri_area_base_height(b, h) – b=base, h=height. Triangle area using base & height.

Example: fm.tri_area_base_height(4, 5) → 10.0

tri_area_sides(a, b, c) – a,b,c=sides. Triangle area using Heron’s formula.

Example: fm.tri_area_sides(3,4,5) → 6.0

tri_perimeter(a, b, c) – a,b,c=sides. Perimeter of triangle.

Example: fm.tri_perimeter(3,4,5) → 12

3️⃣ 3D Geometry

cube_volume(x) – x=side. Volume of cube.

cube_surface_area(x) – x=side. Surface area of cube.

cuboid_volume(l, b, h) – l=length, b=breadth, h=height. Volume of cuboid.

cuboid_surface_area(l, b, h) – Surface area of cuboid.

sphere_volume(r) – r=radius. Volume of sphere.

sphere_surface_area(r) – r=radius. Surface area of sphere.

cylinder_volume(r, h) – r=radius, h=height. Volume of cylinder.

cylinder_surface_area(r, h) – r=radius, h=height. Surface area of cylinder.

cone_volume(r, h) – r=radius, h=height. Volume of cone.

cone_surface_area(r, l) – r=radius, l=slant height. Surface area of cone.

hemisphere_volume(r) – r=radius. Volume of hemisphere.

hemisphere_surface_area(r) – r=radius. Surface area including base.

4️⃣ Algebra

quad_roots(a, b, c) – coefficients of $ax^2 + bx + c = 0$. Returns roots (real or complex).

arithmetic_mean(*args) – Any number of values. Calculates average.

geometric_mean(*args) – Any number of values. Calculates geometric mean.

5️⃣ Trigonometry (Degrees)

sin_deg(x) – Sine of angle $x$.

cos_deg(x) – Cosine of angle $x$.

tan_deg(x) – Tangent of angle $x$.

cosec_deg(x), sec_deg(x), cot_deg(x) – Reciprocal trig functions in degrees.

6️⃣ Physics (Basic)

speed(d, t) – d=distance, t=time.

distance(s, t) – s=speed, t=time.

time(d, s) – d=distance, s=speed.

force(m, a) – m=mass, a=acceleration.

weight(m, g=9.8) – m=mass, g=gravity.

kinetic_energy(m, v) – m=mass, v=velocity.

potential_energy(m, h, g=9.8) – m=mass, h=height.

work(f, d) – f=force, d=distance.

pressure(f, a) – f=force, a=area.

7️⃣ Miscellaneous

factorial(x) – Calculates $x!$.

fibonacci(n) – Returns first $n$ Fibonacci numbers.

nCr(n, r) – Combinations.

nPr(n, r) – Permutations.

📝 Notes

All angles in trigonometry functions are in degrees.

For 3D shapes, input measurements are assumed to be in the same unit.

This library is optimized for school and beginner-level college formulas.

🤝 Contributing

Feel free to fork, submit issues, or suggest new formulas! Pull requests are welcome.

📄 License

MIT License – see LICENSE.txt
