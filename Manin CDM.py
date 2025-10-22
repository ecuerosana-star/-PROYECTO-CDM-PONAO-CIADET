from fastapi import FastAPI
import uvicorn

app = FastAPI()
productos = []

@app.post("/productos")
def crear_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    producto = {"id": len(productos) + 1, "nombre": nombre, "precio": precio}
    productos.append(producto)
    print(producto)

def listar_productos():
    print("Productos:")
    if not productos:
        print("No hay productos")
    for p in productos:
        print(p)

def obtener_producto():
    pid = int(input("Ingrese el ID del producto a buscar: "))
    for p in productos:
        if p["id"] == pid:
            print("Producto encontrado:", p)
            return
    print("Producto no encontrado")

def actualizar_producto():
    pid = int(input("Ingrese el ID del producto a actualizar: "))
    for p in productos:
        if p["id"] == pid:
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_precio = float(input("Nuevo precio: "))
            p["nombre"] = nuevo_nombre
            p["precio"] = nuevo_precio
            print("Producto actualizado")
            return
    print("Producto no encontrado")

def eliminar_producto():
    pid = int(input("Ingrese el ID del producto a eliminar: "))
    for p in productos:
        if p["id"] == pid:
            productos.remove(p)
            print("Producto eliminado")
            return
    print("Producto no encontrado")

def menu():
    while True:
        print("\n1. Crear producto")
        print("2. Listar productos")
        print("3. Obtener producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            obtener_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()

