class Geom:
    def __init__(self, name):
        self.__name = name


class Line(Geom):
    def __init__(self, name, length):
        self.__name = name
        self.__length = length


line = Line('line 1', 10)
geom = Geom('geometry')

print(line)
print(geom)
print(issubclass(Line, Geom))  # проверяет является ли класс Line дочерним для класса Geom. Можно передавать только классы
print(isinstance(line, Geom))  # проверяет является ли объект line дочерним для класса Geom
print(isinstance(geom, object))  # проверяет является ли объект line дочерним для класса Geom


# встроенные типы данных тоже являются классами, следвоательно можно расширять их функционал
# класс Vector наследует весь функционал класса List, но переопределяет метод __str__
class Vector(list):
    def __str__(self):
        return "CLass vector. Length: " + str(len(self))


v = Vector([1,2,3,4])
v.append(10)
v.append(20)
print(v)