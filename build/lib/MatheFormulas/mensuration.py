import math


# 2D FIGURES - AREA AND PERIMETER

def squareArea(side):
    area = side * side
    return area


def squarePerimeter(side):
    perimeter = 4 * side
    return perimeter


def rectangleArea(breadth, height):
    area = breadth * height
    return area


def rectanglePerimeter(breadth, height):
    perimeter = 2 * (breadth + height)
    return perimeter


def triangleArea(base, height):
    area = 0.5 * base * height
    return area


def trianglePerimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter


def circleArea(radius):
    area = math.pi * (radius * radius)
    return area


def circlePerimeter(radius):
    circumference = 2 * math.pi * radius
    return circumference


def ellipseArea(semiMajorAxis, semiMinorAxis):
    area = math.pi * semiMajorAxis * semiMinorAxis
    return area


def ellipsePerimeter(semiMajorAxis, semiMinorAxis):
    perimeter = 2 * math.pi * (math.sqrt(((semiMajorAxis * semiMajorAxis) + (semiMinorAxis * semiMinorAxis)) / 2))
    return perimeter


def rhombusArea(diagonal1, diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return area


def rhombusPerimeter(side):
    perimeter = 4 * side
    return perimeter


def parallelogramArea(base, height):
    area = base * height
    return area


def parallelogramPerimeter(side1, side2):
    perimeter = 2 * (side1 + side2)
    return perimeter


def trapeziumArea(base1, base2, height):
    area = (height / 2) * (base1 + base2)
    return area


def trapeziumPerimeter(side1, side2, side3, side4):
    perimeter = (side1 + side2 + side3 + side4)
    return perimeter


def pentagonArea(side):
    area = (1 / 4) * math.sqrt(5 * (5 + 2 * (math.sqrt(5)))) * (side * side)
    return area


def pentagonPerimeter(side):
    perimeter = (5 * side)
    return perimeter


def hexagonArea(side):
    area = ((3 * math.sqrt(3)) / 2) * (side * side)
    return area


def hexagonPerimeter(side):
    perimeter = (6 * side)
    return perimeter


def heptagonArea(side):
    area = round((7 / 4) * (side * side) * 2.0765213965, 2)
    return area


def heptagonPerimeter(side):
    perimeter = (7 * side)
    return perimeter


def octagonArea(side):
    area = 2 * (1 + math.sqrt(2)) * (side * side)
    return area


def octagonPerimeter(side):
    perimeter = (8 * side)
    return perimeter


def nonagonArea(side):
    area = round((9 / 4) * (side * side) * 2.7474774194, 2)
    return area


def nonagonPerimeter(side):
    perimeter = (9 * side)
    return perimeter


def decagonArea(side):
    area = (5 / 2) * (side * side) * (math.sqrt(5 + 2 * (math.sqrt(5))))
    return area


def decagonPerimeter(side):
    perimeter = (10 * side)
    return perimeter


# 3D FIGURES - VOLUME, CURVED SURFACE AREA, TOTAL SURFACE AREA

def cubeVol(side):
    volume = side * side * side
    return volume


def cubeCsa(side):
    csa = 4 * (side * side)
    return csa


def cubeTsa(side):
    tsa = 6 * (side * side)
    return tsa


def cuboidVol(length, breadth, height):
    volume = length * breadth * height
    return volume


def cuboidCsa(length, breadth, height):
    csa = 2 * height * (length + breadth)
    return csa


def cuboidTsa(length, breadth, height):
    tsa = 2 * ((length * breadth) + (breadth * height) + (height * length))
    return tsa


def cylinderVol(radius, height):
    volume = math.pi * (radius * radius) * height
    return volume


def cylinderCsa(radius, height):
    csa = 2 * math.pi * radius * height
    return csa


def cylinderTsa(radius, height):
    tsa = 2 * math.pi * radius * (radius + height)
    return tsa


def coneVol(radius, height):
    volume = (1 / 3) * math.pi * (radius * radius) * height
    return volume


def coneCsa(radius, length):
    csa = math.pi * radius * length
    return csa


def coneTsa(radius, length):
    tsa = math.pi * radius * (radius + length)
    return tsa


def sphereVol(radius):
    volume = (4 / 3) * math.pi * (radius * radius * radius)
    return volume


def sphereCsa(radius):
    csa = 4 * math.pi * (radius * radius)
    return csa


def sphereTsa(radius):
    tsa = 4 * math.pi * (radius * radius)
    return tsa


def hemisphereVol(radius):
    volume = (2 / 3) * math.pi * (radius * radius * radius)
    return volume


def hemisphereCsa(radius):
    csa = 2 * math.pi * (radius * radius)
    return csa


def hemisphereTsa(radius):
    tsa = 3 * math.pi * (radius * radius)
    return tsa


def ellipsoidVol(radius1, radius2, radius3):
    volume = (4 / 3) * math.pi * radius1 * radius2 * radius3
    return volume


def squarePyramidVol(baseEdge, height):
    volume = (baseEdge * baseEdge) * (height / 3)
    return volume


def pentagonalPyramidVol(baseEdge, height):
    volume = (5 / 12) * 1.376 * height * (baseEdge * baseEdge)
    return volume


def hexagonalPyramidVol(baseEdge, height):
    volume = (math.sqrt(3) / 2) * (baseEdge * baseEdge) * height
    return volume


def triangularPrismVol(base, height, length):
    volume = (1 / 2) * base * height * length
    return volume


def pentagonalPrismVol(base, height, length):
    volume = (5 / 2) * base * height * length
    return volume


def hexagonalPrismVol(base, height):
    volume = (3 / 2) * math.sqrt(3) * (base * base) * height
    return volume


def tetrahedronVol(edge):
    volume = (edge * edge * edge) / (6 * math.sqrt(2))
    return volume


def octahedronVol(edge):
    volume = (math.sqrt(2) / 3) * (edge * edge * edge)
    return volume


def icosahedronVol(edge):
    volume = ((5 * (3 + math.sqrt(5))) / 12) * (edge * edge * edge)
    return volume


def dodecahedronVol(edge):
    volume = ((15 + (7 * math.sqrt(5))) / 4) * (edge * edge * edge)
    return volume


def torusVol(outerRadius, innerRadius):
    if outerRadius > innerRadius:
        volume = (math.pi * innerRadius * innerRadius) * (2 * math.pi * outerRadius)
    else:
        volume = "ERROR - Make sure outer radius is always greater than inner radius"
    return volume
