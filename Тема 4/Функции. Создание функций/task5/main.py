PI = 3.14

def square_circle(r, PI):
    return PI * r ** 2

def length_circle(r, PI):
    return 2 * PI * r


radius = 8  # радиус круга

square = square_circle(radius, PI)
length = length_circle(radius, PI)

print("Площадь равна =", square)
print("Длина окружности равна =", length)
