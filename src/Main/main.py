# main.py

import sys
import os

# Añadir directorios al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from Models.Usuario import Cliente, Administrador
from Models.Producto import Producto, ProductoElectronico, ProductoRopa
from Models.Pedido import Pedido

# Importar TiendaService
tienda_path = os.path.join(os.path.dirname(__file__), '..', 'Tienda Service')
sys.path.insert(0, tienda_path)
from Tienda_service import TiendaService


tienda = TiendaService()

#Ejemplos de clientes y admin 
cliente_1 = tienda.crear_usuario("cliente", 1, "Ramon", "ramon@mail.com", "Calle A")
cliente_2 = tienda.crear_usuario("cliente", 2, "Laura", "laura@mail.com", "Calle B")
cliente_3 = tienda.crear_usuario("cliente", 3, "Mario", "mario@mail.com", "Calle C")
admin = tienda.crear_usuario("administrador", 5, "Admin", "admin@mail.com")


#Ejemplo de 5 productos
p1 = ProductoRopa(101, "Camiseta", 20, 10,"L", "Verde")
p2 = ProductoRopa(102, "Pantalón", 35, 5, "M", "Azul")
p3 = ProductoElectronico(103, "Aurculares", 50, 15, "2 años")
p4 = ProductoElectronico(104, "Altsvoz", 300, 8, "1 año")
p5 = ProductoElectronico(105, "Ordenador", 15, 20, "5 años")

#Añadirlos al inventario
tienda.añadir_producto(p1)
tienda.añadir_producto(p2)
tienda.añadir_producto(p3)
tienda.añadir_producto(p4)
tienda.añadir_producto(p5)

#Stock
print("Stock")
for producto in tienda.ver_productos():
    print(producto)


#Simulacion de pedidos
pedido1 = tienda.realizar_pedido(1, [(p1, 2), (p3, 1)])  
pedido2 = tienda.realizar_pedido(2, [(p2, 1), (p5, 3)])  
pedido3 = tienda.realizar_pedido(3, [(p4, 1), (p5, 2)])  

#Pedidos
print("\nResumen de pedidos")
for pedido in [pedido1, pedido2, pedido3]:
    if pedido:
        print(f"Pedido ID: {pedido.identificador}, Cliente: {pedido.cliente.name}, Total: {pedido.calcular_importe()}€")

#Stock actualizado
print("\nStock actualizado")
for producto in tienda.ver_productos():
    print(producto)

#Historial de compra de Ramon
print("\nTus pedidos")
for pedido in tienda.pedidos:
    if pedido.cliente.identificador == 1:
        print(f"Pedido ID: {pedido.identificador}, Total: {pedido.calcular_importe()}€")
