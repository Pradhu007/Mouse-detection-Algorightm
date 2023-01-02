import time
import pyautogui 
import ctypes

currentpos = 0
previouspos = 0
idlestate = 0 # YOU CAN CHANGE THIS TO HOW LONG YOU WANT IT TO BE!

# Please dont mess with the other variables as the program will not work


# Intialising variables to store mouse information






while True:

   previouspos = currentpos # Stores the previous mouse location as X and Y coords 
   currentpos = pyautogui.position() # Retrieves the current mouse location





   if previouspos != 0:
       # Works fine with this condition so i wont touch it

     if currentpos == previouspos:
      print("Mouse not moving ")
      idlestate = idlestate + 1 # This will increment everytime the mouse is idle(in the same position) 
      ismousemoving = False # Pretty self explanatory 
     else:
      print("Mouse is moving ")
      ismousemoving = True
      idlestate = 0
      # The idle counter is set back to zero when the mouse has stated to move again 

   if idlestate == 5 and ismousemoving == False:
      idlestate = 0
      ctypes.windll.user32.LockWorkStation()
      # Locks your computer if the idle time equals to the one set(by default it is around 5 seconds). 


   time.sleep(1) # Limits CPU usage and contributes to making the program to make a flow. 
   
   
   
   
   
   
   Credits:Pradhu007
   














