from equipos import Equipo

class Cliente:
    def __init__(self, apellidos, nombre, telefono):
        self.__apellidos = apellidos
        self.__nombre = nombre
        self.__telefono = telefono
        self.__equipos = []

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        self.__apellidos = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, value):
        self.__telefono = value

    def agregar_equipo(self, equipo: Equipo):
        self.__equipos.append(equipo)

    def __str__(self):
        return f"{self.__nombre} {self.__apellidos} - Tel: {self.__telefono}"