#~~~ Calculator ~~~
#~~~ IMPORT ~~~
import os 
import time
#~~~ DEF ~~~
def clear():
    os.system('cls')
def time1():
    time.sleep(1.5)
def exit1():
    input('Enter for back')
#~~~ LIST ~~~
list1 ='''What do you want to do :-
1 to Add
2 to Subtract
3 to Multiply
4 to Divide
5 to exit\n'''
#~~~ MAIN-CODE ~~~
while True:
 clear()
 try:
    print(list1)
    type1 =  int(input("Enter Your Value "))
    if type1 == int("1"):
        clear()
        number1 = input("What do you want to Add \n")
        number2 = input(f"{number1} + ")
        print(f"Ans. {float(number1) + float(number2)}")
        exit1()
    elif type1 == int("2"):
        clear()
        number1 = input("What do you want to Subtract \n")
        number2 = input(f"{number1} - ")
        print(f"Ans. {float(number1) - float(number2)}")
        exit1()
    elif type1 == int("3"):
        clear()
        number1 = input("What do you want to Multiply \n")
        number2 = input(f"{number1} * ")
        print(f"Ans. {float(number1) * float(number2)}")
        exit1()
    elif type1 == int("4"):
        clear()
        number1 = input("What do you want to Divide \n")
        number2 = input(f"{number1} / ")
        print(f"Ans. {float(number1) / float(number2)}")
        exit1()
    elif type1 == int("5"):
        clear()
        exit()
    else:
        print(f"I didn't catch you")
 except ValueError:
    clear()
    print('Value-Error')
    time1()
 except KeyboardInterrupt:
    clear()
    print('KeyboardInterrupt-Error')
    time1()


