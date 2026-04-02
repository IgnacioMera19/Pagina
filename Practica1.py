class Videojuego:
    def __init__(self, id, titulo, precio, stock):
        self.id = id
        self.titulo = titulo
        self.precio = precio
        self.stock = stock

class Tienda:
    def __init__(self):
        self.juegos = []
        self.carrito = []
        self.ventas = []

    def agregar_juego(self, juego):
        self.juegos.append(juego)

    def listar_juegos(self):
        for juego in self.juegos:
            print(f"ID: {juego.id} | {juego.titulo} | ${juego.precio} | Stock: {juego.stock}")

    def agregar_al_carrito(self, id_juego, cantidad):
        juego = next((j for j in self.juegos if j.id == id_juego), None)
        if juego and juego.stock >= cantidad:
            self.carrito.append({"juego": juego, "cantidad": cantidad})
            print(f"✓ {juego.titulo} añadido al carrito")
        else:
            print("✗ Producto no disponible")

    def ver_carrito(self):
        total = 0
        for item in self.carrito:
            subtotal = item["juego"].precio * item["cantidad"]
            print(f"{item['juego'].titulo} x{item['cantidad']} = ${subtotal}")
            total += subtotal
        print(f"Total: ${total}")

    def comprar(self):
        total = 0
        for item in self.carrito:
            item["juego"].stock -= item["cantidad"]
            total += item["juego"].precio * item["cantidad"]
        self.ventas.append(total)
        self.carrito = []
        print(f"✓ Compra realizada. Total: ${total}")

# Ejemplo de uso
tienda = Tienda()
tienda.agregar_juego(Videojuego(1, "Batman arkham knight", 60, 10))
tienda.agregar_juego(Videojuego(2, "Detroit become Human", 50, 5))

tienda.listar_juegos()
tienda.agregar_al_carrito(1, 2)
tienda.ver_carrito()
tienda.comprar()