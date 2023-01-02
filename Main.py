import time
import pyautogui 
import ctypes

currentpos = 0 # This cannot be configured 
previouspos = 0 # This cannot be configured 
idlestate = 5 # This can be configured!!! 
counter = 0 # This cannot be configured 


# Please dont mess with the other variables as the program will not work


# Intialising variables to store mouse information






while True:

   previouspos = currentpos # Stores the previous mouse location as X and Y coords 
   currentpos = pyautogui.position() # Retrieves the current mouse location





   if previouspos != 0:
       # Works fine with this condition so i wont touch it

     if currentpos == previouspos:
      print("Mouse not moving ")
      counter = counter + 1 # This will increment everytime the mouse is idle(in the same position) 
      ismousemoving = False # Pretty self explanatory 
     else:
      print("Mouse is moving ")
      ismousemoving = True
      counter = 0 
      # The coun ter is set back to zero when the mouse has started to move again 

   if counter == idlestate and ismousemoving == False:
      counter = 0 
      ctypes.windll.user32.LockWorkStation()
      # Locks your computer if the idle time equals to the one set(by default it is around 5 seconds). 


   time.sleep(1) # Limits CPU usage and contributes to making the program have a smooth flow. 
   
   
   
   
   
   
   #Credits:Pradhu007
   














