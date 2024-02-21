import sys

def main():
    numbers_list = []
    #Get the user's input making sure to delete any missleading whitespaces
    user_input = input("Digite los números que conformarán la lista: ").strip()
    #Store the user's input into a list using split function
    numbers_list = user_input.split(" ")
    #Convert each number in the list to an actual integer instead of a str
    for _ in range(len(numbers_list)):
        try:
            numbers_list[_] = int(numbers_list[_])
        #If any element is not an integer then stop the process and tell the user
        except ValueError:
            sys.exit("Todos los elementos de la lista deben ser números enteros")

    #Print the grouped list using the group_list() function
    print(group_lists(numbers_list))

def group_lists(list:list):
    #These variables are used to check the numbers that have already been evaluated and store the grouped list
    checked_numbers = []
    grouped_numbers = []
    #Process each number individually
    for number in list:
        #If the number has already been processed then continue with the next one
        if number in checked_numbers:
            continue
        #If the number hasn't been processed then
        else:
            #Add the number to the checked list
            checked_numbers.append(number)
            #Count the number of times the number is present in the list
            number_rept = list.count(number)
            #Create a temp list to store the number repeated x times
            temp_list = []
            #Append the number to the temp list number_rept times
            for _ in range(number_rept):
                temp_list.append(number)
            #Append the temp list to the grouped list
            grouped_numbers.append(temp_list)
    
    return grouped_numbers

if __name__ == "__main__":
    main()