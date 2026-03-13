from models import *

personas = []
bebidas = []
postres = []
pedidos = []

# 10 bebidas
bebidas.extend([
    Bebida(1,"Cafe Americano",30,"Grande","Caliente"),
    Bebida(2,"Capuchino",35,"Mediano","Caliente"),
    Bebida(3,"Frappé",40,"Grande","Frío"),
    Bebida(4,"Latte",32,"Mediano","Caliente"),
    Bebida(5,"Mocca",38,"Grande","Caliente"),
    Bebida(6,"Té Verde",25,"Mediano","Caliente"),
    Bebida(7,"Chocolate Caliente",30,"Grande","Caliente"),
    Bebida(8,"Smoothie Fresa",42,"Grande","Frío"),
    Bebida(9,"Smoothie Mango",42,"Grande","Frío"),
    Bebida(10,"Capuchino Vainilla",36,"Mediano","Caliente"),
])

# 10 postres
postres.extend([
    Postre(1,"Pastel de Chocolate",25),
    Postre(2,"Galleta",10),
    Postre(3,"Muffin",20),
    Postre(4,"Cheesecake",30),
    Postre(5,"Brownie",22),
    Postre(6,"Donut",15),
    Postre(7,"Panqueque",18),
    Postre(8,"Cupcake",20),
    Postre(9,"Tarta de Frutas",28),
    Postre(10,"Gelatina",12),
])

# 10 clientes
for i, nombre in enumerate(["Ana","Luis","Carlos","Maria","Pedro","Laura","Jorge","Sofia","Diego","Elena"], start=1):
    cliente = Cliente(i, nombre, f"{nombre.lower()}@mail.com")
    personas.append(cliente)

# 10 empleados
for i, (nombre, rol) in enumerate([("Juan","BARISTA"),("Rosa","MESERO"),("Mario","GERENTE"),
                                ("Julia","BARISTA"),("Pablo","MESERO"),("Carla","BARISTA"),
                                ("Miguel","MESERO"),("Valeria","GERENTE"),("Fernando","BARISTA"),
                                ("Lucia","MESERO")], start=11):
    personas.append(Empleado(i, nombre, f"{nombre.lower()}@mail.com", f"E{i-10:02}", rol))



pedido_id = 1
for cliente in [p for p in personas if isinstance(p, Cliente)]:
    pedido = Pedido(pedido_id)
    # cada cliente recibe una bebida y un postre
    pedido.agregarProducto(bebidas[(pedido_id-1)%10])
    pedido.agregarProducto(postres[(pedido_id-1)%10])
    pedido.calcularTotal()
    pedidos.append(pedido)
    cliente.realizarPedido(pedido)
    pedido_id += 1



def registrarCliente():
    idPersona = len(personas) + 1
    nombre = input("Nombre: ")
    email = input("Email: ")
    personas.append(Cliente(idPersona, nombre, email))
    print(f"Cliente registrado con ID {idPersona}")

def registrarEmpleado():
    idPersona = len(personas) + 1
    nombre = input("Nombre: ")
    email = input("Email: ")
    idEmpleado = input("ID Empleado: ")
    rol = input("Rol: ")
    personas.append(Empleado(idPersona, nombre, email, idEmpleado, rol))
    print(f"Empleado registrado con ID {idPersona}")

def mostrarProductos():
    print("\n--- Bebidas ---")
    for i, b in enumerate(bebidas):
        print(f"{i+1} - {b.nombre} ${b.precioBase}")
    print("\n--- Postres ---")
    for i, p in enumerate(postres):
        print(f"{i+1} - {p.nombre} ${p.precioBase}")

def crearPedidoCliente():
    print("\nClientes registrados:")
    for p in personas:
        if isinstance(p, Cliente):
            print(f"{p.idPersona} - {p.nombre}")
    idCliente = int(input("ID del cliente que realiza el pedido: "))
    cliente = None
    for p in personas:
        if isinstance(p, Cliente) and p.idPersona == idCliente:
            cliente = p
            break
    if not cliente:
        print("Cliente no encontrado")
        return

    pedido = Pedido(len(pedidos) + 1)

    while True:
        mostrarProductos()
        tipo = input("Agregar Bebida o Postre? (b/p): ").lower()
        if tipo == "b":
            op = int(input("Número de bebida: ")) - 1
            if 0 <= op < len(bebidas):
                pedido.agregarProducto(bebidas[op])
        elif tipo == "p":
            op = int(input("Número de postre: ")) - 1
            if 0 <= op < len(postres):
                pedido.agregarProducto(postres[op])
        else:
            print("Opción inválida")
            continue
        mas = input("¿Agregar otro producto? (si/no): ").lower()
        if mas != "si":
            break

    pedido.calcularTotal()
    pedidos.append(pedido)
    cliente.realizarPedido(pedido)
    print("\n--- Resumen del pedido ---")
    for pr in pedido.productos:
        precio = pr.calcularPrecioFinal() if isinstance(pr, Bebida) else pr.precioBase
        print(f"{pr.nombre} - ${precio}")
    print(f"Total a pagar: ${pedido.total}")

def verHistorialCliente():
    print("\nClientes registrados:")
    for p in personas:
        if isinstance(p, Cliente):
            print(f"{p.idPersona} - {p.nombre}")
    idCliente = int(input("ID del cliente para ver historial: "))
    cliente = None
    for p in personas:
        if isinstance(p, Cliente) and p.idPersona == idCliente:
            cliente = p
            break
    if not cliente:
        print("Cliente no encontrado")
        return
    print(cliente.verHistorial())

def verClientesEmpleado():
    print("\nClientes registrados:")
    for p in personas:
        if isinstance(p, Cliente):
            print(f"{p.idPersona} - {p.nombre} - {p.email}")

def eliminarClienteEmpleado():
    idCliente = int(input("ID del cliente a eliminar: "))
    for p in personas:
        if isinstance(p, Cliente) and p.idPersona == idCliente:
            personas.remove(p)
            for ped in list(p.historialPedidos):
                if ped in pedidos:
                    pedidos.remove(ped)
            print("Cliente y pedidos eliminados")
            return
    print("Cliente no encontrado")

def verPedidosEmpleado():
    if not pedidos:
        print("No hay pedidos")
        return
    for ped in pedidos:
        print(f"\nPedido {ped.idPedido}:")
        for pr in ped.productos:
            precio = pr.calcularPrecioFinal() if isinstance(pr, Bebida) else pr.precioBase
            print(f" - {pr.nombre} ${precio}")
        print(f"Total: ${ped.total}")

def eliminarPedidoEmpleado():
    idPedido = int(input("ID del pedido a eliminar: "))
    for ped in pedidos:
        if ped.idPedido == idPedido:
            pedidos.remove(ped)
            print("Pedido eliminado")
            return
    print("Pedido no encontrado")

while True:
    print("\n--- CAFETERIA ---")
    print("1 Registrar Cliente")
    print("2 Registrar Empleado")
    print("3 Hacer pedido (Cliente)")
    print("4 Ver historial (Cliente)")
    print("5 Ver clientes (Empleado)")
    print("6 Eliminar cliente (Empleado)")
    print("7 Ver pedidos (Empleado)")
    print("8 Eliminar pedido (Empleado)")
    print("9 Salir")

    op = input("Opción: ")

    if op == "1":
        registrarCliente()
    elif op == "2":
        registrarEmpleado()
    elif op == "3":
        crearPedidoCliente()
    elif op == "4":
        verHistorialCliente()
    elif op == "5":
        verClientesEmpleado()
    elif op == "6":
        eliminarClienteEmpleado()
    elif op == "7":
        verPedidosEmpleado()
    elif op == "8":
        eliminarPedidoEmpleado()
    elif op == "9":
        break
    else:
        print("Opción inválida")