
#Set the groups provided by the exercise
product_groups = ["dairy", "cleaning", "grain"]

#Create lists for each category
dairy_products = []
cleaning_products = []
grain_products = []

#Create lists for the quantity of each category
dairy_product_qtys = []
cleaning_product_qtys = []
grain_product_qtys = []

def main():

    #Variable to control the flow of the program
    run_program = True
    while run_program:
        #Print the options to the user
        print(
            "Sistema de inventario. Ingrese una opción:",
            "------------------------------------------",
            "1. Agregar producto",
            "2. Ver reporte de inventario",
            "3. Salir", sep="\n", end="\n"
            )
        user_option = input("Su opción: ")
        #If the user wants to add a product, call add_product()
        if user_option == "1":
            add_product()
        if user_option == "2":
            show_inventory()
        if user_option == "3":
            run_program = False
    
#This function adds a new product or updates an existing one
def add_product():
    #Ask the user's input for the product name and quantity to be added
    prod_name = input("Ingrese el nombre del producto que desea agregar: ")
    prod_qty = input("Ingrese la cantidad del producto que desea agregar: ")
    #Check if the product already exists in dairy products
    if prod_name in dairy_products:
        #Check for the index to match the quantity list
        index = dairy_products.index(prod_name)
        try:
            #Add the new quantity to the one that already exists thus updating the total quantity
            dairy_product_qtys[index] += int(prod_qty)
        #If the user input is invalid, notify them and continue running the program
        except ValueError:
            print("No es posible añadir un valor no numérico o decimal a los productos")
            exit
    #Repeat the logic above for cleaning products
    elif prod_name in cleaning_products:
        index = cleaning_products.index(prod_name)
        try:
            cleaning_product_qtys[index] += int(prod_qty)
        except ValueError:
            print("No es posible añadir un valor no numérico o decimal a los productos")
            exit
    #Repeat the logic above for grain products
    elif prod_name in grain_products:
        index = grain_products.index(prod_name)
        try:
            grain_product_qtys[index] += int(prod_qty)
        except ValueError:
            print("No es posible añadir un valor no numérico o decimal a los productos")
            exit
    #If the product doesn't exist in any category yet, ask the user for the category
    else:
        prod_group = input("Ingrese el grupo al que pertenece el producto que desea agregar: ")
        #If the category is valid, add the new product and qty to it's corresponding list
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
            #If the category is invalid, notify the user and continue running the program
            case _:
                print("El nombre de grupo ingresado es  invalido")
                exit
            
    print("Producto añadido/actualizado correctamente ", end="\n")
    
#This function prints the total inventory with product names and it's quantities
def show_inventory():

    #Get the largest str between all lists to format the printing afterwards
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
    #Print each dairy product and it's quantity alligning it to the left taking into account the max lenght str
    for _ in range(len(dairy_products)):
        print(f"{dairy_products[_].ljust(max_length)}\t\t\t{dairy_product_qtys[_]}")
    #Apply same logic for the cleaning products 
    for _ in range(len(cleaning_products)):
        print(f"{cleaning_products[_].ljust(max_length)}\t\t\t{cleaning_product_qtys[_]}")
    #Apply same logic for the grain products
    for _ in range(len(grain_products)):
        print(f"{grain_products[_].ljust(max_length)}\t\t\t{grain_product_qtys[_]}")
    print(
        '''
------------------------------------------
        '''
        )
    
if __name__ == "__main__":
    main()