# Collaborators (including web sites where you got help: (enter none if you didn't need help) = mom 
#  

def factorial_calc(number):   #you may choose the name of the parameter

    answer = 1

    if your_number < 0:
        print("There is no factorial for negative numbers")
    elif your_number == 0:
        print("Factorial of 0 is 1")
    else: 
        for x in range(1, your_number + 1):
            answer = answer * x
            

    return answer    # be sure to return the factorial


if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values

    your_number = int(input("Input a number that you would like to know the factorial of... "))

    print(factorial_calc(int(your_number)))

    # After you are satisfied with your results, use input() to prompt the user for a value:
    #num = input("Enter value to factorialize: ")
    #print(factorial_calc(int(num)))
