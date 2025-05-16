class Equipo:
    def __init__(self, numero, tipo, descripcion):
        self.__numero = numero
        self.__tipo = tipo
        self.__descripcion = descripcion

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, value):
        self.__descripcion = value

    def __str__(self):
        return f"{self.__tipo} (N°: {self.__numero} - Problema: {self.__descripcion})"
