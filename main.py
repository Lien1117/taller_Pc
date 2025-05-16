from clientes import Cliente
from equipos import Equipo

clientes = []

def ingresar_cliente_con_equipo():
    print("\n-- Ingresar nuevo cliente y su equipo --")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")

    c = Cliente(apellido, nombre, telefono)

    numero = input("Número de parte del equipo: ")
    tipo = input("Tipo de equipo (ej. portátil, celular, etc.): ")
    descripcion = input("Descripción del problema: ")

    eq = Equipo(numero, tipo, descripcion)
    c.agregar_equipo(eq)

    clientes.append(c)
    print("Cliente y equipo registrados exitosamente.")

def ver_clientes():
    if not clientes:
        print("No hay clientes registrados.")
        return
    print("\n-- Lista de Clientes --")
    for i, cliente in enumerate(clientes, 1):
        print(f"{i}. {cliente}")

def ver_equipos_de_cliente():
    ver_clientes()
    if not clientes:
        return
    try:
        index = int(input("Seleccione el número del cliente: ")) - 1
        if 0 <= index < len(clientes):
            cliente = clientes[index]
            print(f"\nEquipos de {cliente.nombre} {cliente.apellidos}:")
            equipos = cliente.equipos
            if not equipos:
                print("Este cliente no tiene equipos registrados.")
            else:
                for equipo in equipos:
                    print(f" - {equipo}")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Ingresar cliente con equipo")
        print("2. Ver clientes")
        print("3. Ver equipos por cliente")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ingresar_cliente_con_equipo()
        elif opcion == '2':
            ver_clientes()
        elif opcion == '3':
            ver_equipos_de_cliente()
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()