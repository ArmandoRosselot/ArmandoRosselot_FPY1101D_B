# Armando Rosselot

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {
    '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
    'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}

# Funciones
def stock_marca():
    mod=input("Ingrese modelo a buscar su stock: ")
    for modelo in stock:
        if modelo == mod:
            print(f"el stock de {modelo} es {stock[modelo][1]}")
    if mod not in modelo:
        print("Stock del producto no encontrado, intente nuevamente.")

def busqueda_precio():
    while True:
        try:
            precio_min=int(input("ingrese percio mínimo: "))
            if precio_min < 0:
                print("el precio minimo debe ser un valor mayor a 0")
            else:
                break
        except ValueError:
            print("el precio minimo debe ser un número entero")
    while True:
        try:
            precio_max=int(input("ingrese precio máximo: "))
            if precio_max < 0:
                print("el precio maximo debe ser un valor mayor a 0")
            elif precio_min > precio_max:
                print("el precio máximo debe ser mayor al precio mínimo")
            else:
                break
        except ValueError:
            print("el precio máximo debe ser un numero entero")
    lista_modelos=[]
    for modelo in stock:
        if stock[modelo][0] > precio_min and stock[modelo][0] < precio_max:
            lista_modelos.append(modelo)
            lista_modelos.sort()
        if lista_modelos == []:
                print("No hay notebooks en ese rango de precios.")
                return
    print(f"Los notebooks entre los precios consultas son: {lista_modelos}")
        
def eliminar_producto():
    while True:
        mod=input("Ingrese modelo a eliminar: ")
        for modelo in productos:
            if mod == modelo:
                del productos[modelo]
                print(f"Producto {modelo} eliminado con exito.")
                return
        if mod not in modelo:
            print("Modelo no existe!!! Intente nuevamente.")
            
def main():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Eliminar producto.")
        print("4. Salir.")
        opcion=input("Ingrese una opción: ")
        if opcion == "1":
            stock_marca()
        elif opcion == "2":
            busqueda_precio()
        elif opcion == "3":
            while True:
                eliminar_producto()
                opc = input("¿Desea eliminar otro producto? (ingrese 's/n'): ").lower()
                if opc == "s":
                    continue
                if opc == "n":
                    break
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción incorrecta, vuelva a intentarlo")
    

if __name__ == "__main__":
    main()