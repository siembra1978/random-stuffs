import time

n=0
while True:
   test = 3*n + 1
   if ((test % 2) == 0):
      print("even")
   else:
      print("odd")
   n+=1
   time.sleep(.125)