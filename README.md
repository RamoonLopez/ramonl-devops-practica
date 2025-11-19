# Tienda Service - Docker

## a. Cómo construir la imagen

```bash
docker build -t tienda-app:latest .
```

## b. Cómo ejecutar la aplicación

```bash
docker run tienda-app:latest
```

## c. Variables de entorno soportadas

No requiere variables de entorno.

## d. Salida esperada

```
Stock
Identificador: 101, Name: Camiseta, Price: 20, Stock: 10, Size: L, Colour: Verde
Identificador: 102, Name: Pantalón, Price: 35, Stock: 5, Size: M, Colour: Azul
Identificador: 103, Name: Aurculares, Price: 50, Stock: 15, Garantia: 2 años
Identificador: 104, Name: Altsvoz, Price: 300, Stock: 8, Garantia: 1 año
Identificador: 105, Name: Ordenador, Price: 15, Stock: 20, Garantia: 5 años

Resumen de pedidos
Pedido ID: 1, Cliente: Ramon, Total: 90€
Pedido ID: 2, Cliente: Laura, Total: 80€
Pedido ID: 3, Cliente: Mario, Total: 330€

Stock actualizado
Identificador: 101, Name: Camiseta, Price: 20, Stock: 8, Size: L, Colour: Verde
Identificador: 102, Name: Pantalón, Price: 35, Stock: 4, Size: M, Colour: Azul
Identificador: 103, Name: Aurculares, Price: 50, Stock: 14, Garantia: 2 años
Identificador: 104, Name: Altsvoz, Price: 300, Stock: 7, Garantia: 1 año
Identificador: 105, Name: Ordenador, Price: 15, Stock: 15, Garantia: 5 años

Tus pedidos
Pedido ID: 1, Total: 90€
```
