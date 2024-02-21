import sys

def main():
    #Check if the repetitions number is more than zero
    if int(sys.argv[2]) <= 0:
        sys.exit("El número de repeticiones debe ser mayor a 0")
    else:
        #Check if the user's number is negative
        is_negative = int(sys.argv[1]) < 0
        total_sum = 0
        #If it is, remove the "-" and add it at the end of the process
        if is_negative:
            sys.argv[1] = sys.argv[1].removeprefix("-")

        #Iterate through the number of repetitions provided by the user
        for _ in range(int(sys.argv[2])):
            try:
                #The new number to be added will be the number provided by the user repeated x times
                new_number = sys.argv[1] * (_+1)
                #Store the total sum
                total_sum += int(new_number)
            #In case the input provided by the user is a word or a float number
            except ValueError:
                sys.exit("Uno de los valores introducidos no es un número o no es un valor entero")
        #Add the "-" to the number if it is negative, else print normally
        if is_negative:
            print(f"-{total_sum}")
        else:
            print(total_sum)


if __name__ == "__main__":
    main()

