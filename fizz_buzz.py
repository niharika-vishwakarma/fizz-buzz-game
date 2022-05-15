#multiple of 3 will print -fizz 
#multiple of  will print -buzz
#multiple of 3&5 will print -fizz-buzz 

def fizzbuzz(r):
    for i in range(1,r):
         if (i%3==0 and i%5==0):
           print(i,"fizz-buzz")
         elif (i%5==0):
           print(i,"buzz")
         elif (i%3==0):
           print(i,"fizz")
         else:
            print(i,"empty")

fizzbuzz(34)
