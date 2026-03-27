import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        # Разность координат для получения вектора
        return Point(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        # Скалярное произведение
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        # Векторное произведение
        return Point(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )

    def absolute(self):
        # Длина (модуль) вектора
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

def plane_angle(A, B, C, D):
    # 1. Находим векторы согласно условию
    # В стандартной геометрии BC обычно C-B, но следуем формулам из условия
    AB = B - A
    BC = C - B
    CD = D - C

    # 2. Находим нормали к плоскостям через векторное произведение
    X = AB.cross(BC)
    Y = BC.cross(CD)

    # 3. Вычисляем косинус угла по формуле: cos(phi) = (X,Y) / (|X||Y|)
    cos_phi = X.dot(Y) / (X.absolute() * Y.absolute())

    # Ограничиваем значение косинуса диапазоном [-1, 1] во избежание ошибок math.acos
    cos_phi = max(-1.0, min(1.0, cos_phi))

    # 4. Находим угол в радианах и переводим в градусы
    phi_rad = math.acos(cos_phi)
    return math.degrees(phi_rad)

if __name__ == '__main__':
    # Считывание данных (ожидается 4 строки по 3 координаты)
    points = []
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(Point(*a))

    A, B, C, D = points
    angle = plane_angle(A, B, C, D)
    print(f"{angle:.2f}")