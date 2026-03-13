# =========================
# MODELOS
# =========================

class Persona:
    def __init__(self,idPersona,nombre,email):
        self.idPersona=idPersona
        self.nombre=nombre
        self.email=email

class Cliente(Persona):
    def __init__(self,idPersona,nombre,email):
        super().__init__(idPersona,nombre,email)
        self.historialPedidos=[]

    def realizarPedido(self,pedido):
        self.historialPedidos.append(pedido)
        return f"Pedido {pedido.idPedido} registrado"

    def verHistorial(self):
        if not self.historialPedidos:
            return "No tiene pedidos"
        texto=""
        for p in self.historialPedidos:
            texto+=f"\nPedido {p.idPedido}:\n"
            for pr in p.productos:
                if isinstance(pr,Bebida):
                    precio=pr.calcularPrecioFinal()
                else:
                    precio=pr.precioBase
                texto+=f" - {pr.nombre}: ${precio}\n"
            texto+=f"Total a pagar: ${p.total}\n"
        return texto

class Empleado(Persona):
    def __init__(self,idPersona,nombre,email,idEmpleado,rol):
        super().__init__(idPersona,nombre,email)
        self.idEmpleado=idEmpleado
        self.rol=rol

class ProductoBase:
    def __init__(self,idProducto,nombre,precioBase):
        self.idProducto=idProducto
        self.nombre=nombre
        self.precioBase=precioBase

class Bebida(ProductoBase):
    def __init__(self,idProducto,nombre,precioBase,tamano,temperatura):
        super().__init__(idProducto,nombre,precioBase)
        self.tamano=tamano
        self.temperatura=temperatura
        self.modificadores=[]

    def agregarExtra(self,extra):
        self.modificadores.append(extra)

    def calcularPrecioFinal(self):
        return self.precioBase + len(self.modificadores)*5

class Postre(ProductoBase):
    def __init__(self,idProducto,nombre,precioBase,esVegano=False,sinGluten=False):
        super().__init__(idProducto,nombre,precioBase)
        self.esVegano=esVegano
        self.sinGluten=sinGluten

class Pedido:
    def __init__(self,idPedido):
        self.idPedido=idPedido
        self.productos=[]
        self.total=0

    def agregarProducto(self,producto):
        self.productos.append(producto)

    def calcularTotal(self):
        total=0
        for p in self.productos:
            if isinstance(p,Bebida):
                total+=p.calcularPrecioFinal()
            else:
                total+=p.precioBase
        self.total=total
        return total