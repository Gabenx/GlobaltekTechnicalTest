product_groups = ["dairy", "cleaning", "grain"]

dairy_products = []
cleaning_products = []
grain_products = []

dairy_product_qtys = []
cleaning_product_qtys = []
grain_product_qtys = []

def main():

    run_program = True
    while run_program:
        print(
            "Sistema de inventario. Ingrese una opción:",
            "------------------------------------------",
            "1. Agregar producto",
            "2. Ver reporte de inventario",
            "3. Salir", sep="\n", end="\n"
            )
        user_option = input("Su opción: ")
        if user_option == "1":
            add_product()
        if user_option == "2":
            show_inventory()
        if user_option == "3":
            run_program = False
    

def add_product():
    prod_name = input("Ingrese el nombre del producto que desea agregar: ")
    prod_qty = input("Ingrese la cantidad del producto que desea agregar: ")
    
    if prod_name in dairy_products:
        index = dairy_products.index(prod_name)
        try:
            dairy_product_qtys[index] += int(prod_qty)
        except ValueError:
            print("No es posible añadir un valor no numérico o decimal a los productos")
            exit
    
    elif prod_name in cleaning_products:
        index = cleaning_products.index(prod_name)
        try:
            cleaning_product_qtys[index] += int(prod_qty)
        except ValueError:
            print("No es posible añadir un valor no numérico o decimal a los productos")
            exit

    elif prod_name in grain_products:
        index = grain_products.index(prod_name)
        try:
            grain_product_qtys[index] += int(prod_qty)
        except ValueError:
            print("No es posible añadir un valor no numérico o decimal a los productos")
            exit
    else:
        prod_group = input("Ingrese el grupo al que pertenece el producto que desea agregar: ")
        match prod_group.lower():
            case "dairy":
                dairy_products.append(prod_name)
                dairy_product_qtys.append(int(prod_qty))

            case "cleaning":
                cleaning_products.append(prod_name)
                cleaning_product_qtys.append(int(prod_qty))

            case "grain":
                grain_products.append(prod_name)
                grain_product_qtys.append(int(prod_qty))
            
            case _:
                print("El nombre de grupo ingresado es  invalido")
            
    print("Producto añadido/actualizado correctamente ", end="\n")
    

def show_inventory():

    max_length = 0
    for product_list in [dairy_products, cleaning_products, grain_products]:
        for product in product_list:
            max_length = max(max_length, len(product))

    print(
        '''
Nombre                          Existencias
------------------------------------------
        '''
        )
    for _ in range(len(dairy_products)):
        print(f"{dairy_products[_].ljust(max_length)}\t\t\t{dairy_product_qtys[_]}")
    for _ in range(len(cleaning_products)):
        print(f"{cleaning_products[_].ljust(max_length)}\t\t\t{cleaning_product_qtys[_]}")
    for _ in range(len(grain_products)):
        print(f"{grain_products[_].ljust(max_length)}\t\t\t{grain_product_qtys[_]}")
    print(
        '''
------------------------------------------
        '''
        )
    
if __name__ == "__main__":
    main()