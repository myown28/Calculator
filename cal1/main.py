# calculatot
import os

def esc():
    B1 = input("exit enter y \n")
    if B1 == 'Y' or 'y':
            print("ok")


#home page
while True:
    os.system('cls')
    print("calculatot")
    print("for Add enter 1 \n" + "for Subtract enter 2 \n" + "for Multiply enter 3 \n" + "for Divide enter 4 \n" + "exit enter e ")
    A1 = input('\n')

    # exit
    if A1 == 'e' or 'E':
        exit()
    
    # Add
    elif A1 == '1':
        print("\n~~~ Add ~~~")
        number1 = int(input('What do you want to Add \n'))
        number2 = int(input(f'{number1} + '))
        print(f"Ans. {float(number1) + float(number2)}\n") 
        esc()
        

    # Subtract
    elif A1 == '2':
        print("\n~~~ Subtract ~~~")
        number1 = int(input('What do you want to Subtract \n'))
        number2 = int(input(f'{number1} - '))
        print(f"Ans. {float(number1) - float(number2)}\n")
        esc()

    # multipy      
    elif A1 == '3':
        print("\n~~~ Multiply ~~~")
        number1 = int(input('What do you want to Multiply \n'))
        number2 = int(input(f'{number1} × '))
        print(f"Ans. {float(number1) * float(number2)}\n")
        esc()

    # divide
    elif A1 == '4':
        print("\n~~~ Divide ~~~")
        number1 = int(input('What do you want to Divide \n'))
        number2 = int(input(f'{number1} ÷ '))
        print(f"Ans. {float(number1) / float(number2)}\n")
        esc()

    # error
    else:
        print(f"I didn't catch you")

    
