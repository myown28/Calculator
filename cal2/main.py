#~~~ Pratham-code ~~~
# calculatot
import os
import time 

def esc():
    B1 = input("exit enter \n")
    if B1 == 'Y' or 'y':
            print("ok")
    else:
         exit()

#home page
while True:
    os.system('cls')
    print("calculatot")
    P1 = ("for Add enter 1 (+)\n" + "for Subtract enter 2 (-)\n" + "for Multiply enter 3 (×)\n" + "for Divide enter 4 (÷)\n" + "for exit enter E\n" )
    A1 = input(P1)
 
    if A1 == "1":
        print("\n~~~ Add ~~~")
        number1 = int(input('What do you want to Add \n'))
        number2 = int(input(f'{number1} + '))
        print(f"Ans. {float(number1) + float(number2)}\n") 
        esc()

    elif A1 == '2':
        print("\n~~~ Subtract ~~~")
        number1 = int(input('What do you want to Subtract \n'))
        number2 = int(input(f'{number1} - '))
        print(f"Ans. {float(number1) - float(number2)}\n")
        esc()

    elif A1 == '3':
        print("\n~~~ Multiply ~~~")
        number1 = int(input('What do you want to Multiply \n'))
        number2 = int(input(f'{number1} × '))
        print(f"Ans. {float(number1) * float(number2)}\n")
        esc()

    elif A1 == '4':
        print("\n~~~ Divide ~~~")
        number1 = int(input('What do you want to Divide \n'))
        number2 = int(input(f'{number1} ÷ '))
        print(f"Ans. {float(number1) / float(number2)}\n")
        esc()

    elif A1 == "E" or "e":
        print('OK')
        time.sleep(1)
        exit()

    else:
        print("not foung")

         

    
