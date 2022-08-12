from setuptools import setup, find_packages

VERSION = '1.0'
DESCRIPTION = 'Math mensuration formulas'
LONG_DESCRIPTION = 'This package is deigned to find area and perimeter of 2D figures like ' \
                   'square, rectangle, triangle, circle, ellipse, rhombus, parallelogram, trapezium, pentagon, ' \
                   'hexagon, heptagon, octagon, nonagon and decagon ' \
                   'You can also find volume, Total surface area and Curved surface are of 3D Figures like' \
                   'cube, cuboid, cylinder, cone, sphere, hemisphere, ellipsoid, squarePyramid, pentagonalPyramid,' \
                   'hexagonalPyramid, triangularPrism, pentagonalPrism, hexagonalPrism, tetrahedron, octahedron,' \
                   'icosahedron, dodecahedron and torus '

# Setting up
setup(
    name="MatheFormulas",
    version=VERSION,
    author="CoderMadhuresh",
    author_email="madhureshgupta1234@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'python3', 'math', 'formulas', 'mensuration', 'MatheFormulas', 'coder', 'Madhuresh'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
