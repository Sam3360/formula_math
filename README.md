🧮 Formula Math (formula_math)

Formula Math is a comprehensive Python library designed to make math, physics, finance, and geometry formulas instantly accessible. Perfect for students, teachers, and developers to save time and avoid remembering complex equations.

🎯 Target Audience & Benefits

Who is this for?

Students: Simplify homework and verify calculations.

Educators: Use as a teaching tool for Python applications.

Developers: Lightweight utility for quick logic without heavy dependencies.

Why use formula_math?

Save Time: No need to look up constants like PI or Gravity.

Accuracy: Built-in logic handles edge cases automatically.

Readability: Clean and intuitive function names.

🚀 Key Features

Finance: Simple and compound interest.

Geometry: 2D Areas/Perimeters and 3D Volumes/Surface Areas.

Physics: Kinematics, dynamics, energy, and pressure.

Algebra: Quadratic roots and various means.

Trigonometry: Degree-based functions.

Misc: Factorials, Fibonacci, and Combinatorics.

📦 Installation

pip install formula_math


🛠 Usage

import formula_math as fm

# Example: Calculate the area of a circle with radius 7
result = fm.circle_area(7)
print(result) # Output: 153.938


📚 API Reference

1️⃣ Finance Formulas

si(p, r, t) – p=Principal, r=Rate %, t=Time (yrs). Simple Interest.

ci(p, r, t) – p=Principal, r=Rate %, t=Time (yrs). Compound Interest.

2️⃣ 2D Geometry

sq_perimeter(x) – x=side. Perimeter of a square.

sq_area(x) – x=side. Area of a square.

rect_perimeter(l, b) – l=length, b=breadth. Perimeter of a rectangle.

rect_area(l, b) – l=length, b=breadth. Area of a rectangle.

circle_area(r) – r=radius. Area of a circle.

circle_circumference(r) – r=radius. Circumference of a circle.

tri_area_base_height(b, h) – b=base, h=height. Triangle area.

tri_area_sides(a, b, c) – a,b,c=sides. Heron’s formula.

tri_perimeter(a, b, c) – a,b,c=sides. Perimeter of triangle.

3️⃣ 3D Geometry

cube_volume(x) – x=side.

cube_surface_area(x) – x=side.

cuboid_volume(l, b, h) – Volume of cuboid.

cuboid_surface_area(l, b, h) – Surface area.

sphere_volume(r) – Volume of sphere.

sphere_surface_area(r) – Surface area.

cylinder_volume(r, h) – Volume.

cylinder_surface_area(r, h) – Surface area.

cone_volume(r, h) – Volume.

cone_surface_area(r, l) – Surface area.

hemisphere_volume(r) – Volume.

hemisphere_surface_area(r) – Surface area.

4️⃣ Algebra

quad_roots(a, b, c) – Coefficients of $ax^2 + bx + c = 0$.

arithmetic_mean(*args) – Calculates average.

geometric_mean(*args) – Calculates geometric mean.

5️⃣ Trigonometry (Degrees)

sin_deg(x), cos_deg(x), tan_deg(x) – Standard trig.

cosec_deg(x), sec_deg(x), cot_deg(x) – Reciprocal trig.

6️⃣ Physics (Basic)

speed(d, t), distance(s, t), time(d, s) – Kinematics.

force(m, a), weight(m, g=9.8) – Dynamics.

kinetic_energy(m, v), potential_energy(m, h, g=9.8) – Energy.

work(f, d), pressure(f, a) – Work and Pressure.

7️⃣ Miscellaneous

factorial(x) – Factorial $x!$.

fibonacci(n) – Fibonacci sequence up to $n$ terms.

nCr(n, r) – Combinations.

nPr(n, r) – Permutations.

📝 Notes

All trigonometry functions use degrees.

Ensure all measurements are in consistent units.

Optimized for school and beginner college levels.

📄 License

Distributed under the MIT License.
