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
    
    #Print the filtered list using the list_conditions() function
    print(list_conditions(numbers_list))

#This function returns the list that satisfies all conditions
def list_conditions(list:list):

    output_list = []
    #Evaluate each number for each condition
    for number in list:
        #If the number is > 1000 stop the execution and return the result
        if number > 1000:
            break
        #If the number is > 600 ignore it
        elif number > 600:
            continue
        #If the number is divisible by 5 then store it in the output list
        elif number%5 == 0:
            output_list.append(number)

    return output_list
    
if __name__ == "__main__":
    main()