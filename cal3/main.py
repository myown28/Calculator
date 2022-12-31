import os
import time 
from myown.BPack import cal

#def
def esc():
     B1 = input("exit enter y \n")
     if B1 == 'Y' or 'y':
      print("ok")

#home page
while True:
    os.system('cls')
    print("calculatot")
    P1 = ("for Add enter 1 (+)\n" + 
          "for Subtract enter 2 (-)\n" + 
          "for Multiply enter 3 (×)\n" + 
          "for Divide enter 4 (÷)\n" + 
          "for exit 🟥 enter E\n" )
    A1 = input(P1)
 
    if A1 == "1":
      cal.add()
      cal.esc()

    elif A1 == '2':
       cal.subtract()  
       cal.esc()

    elif A1 == '3':
       cal.multiply()
       cal.esc()

    elif A1 == '4':
       cal.divide()
       cal.esc()

    elif A1 == "E" or "e":
       print('OK ✅')
       time.sleep(2.5)
       exit()

    else:
      print(f"I didn't catch you")
      
    
    