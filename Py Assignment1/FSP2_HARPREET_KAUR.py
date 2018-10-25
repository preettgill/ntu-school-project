#1.User inputs (assuming positive) integer, int num
#2.Check if num is not larger than the maximum allowable value for integer (i.e. 2147483647 which is (2^31)-1)
#3.Check if num is Prime,Square and Fibonacci number
#4.Print statements

import math

#1.
num= int(raw_input("Input a number:"))

      
#2.
if num < 2147483647:
        #if statements to check if num is a prime number or not a prime number
        if num > 2:
                #for loop to check if num prime number
                for p in range(2,(num+1)):
                #for p in range(3,int((num**0.5)+1),2):
                        if num % p == 0:
                                print "It is not a prime number"
                                break
                        else:
                                print "It is a prime number"
                                break
        #if num is 2
        if num == 2:
                print "It is a prime number"
        #if num is less than 2 (i.e. 1,0)
        if num < 2:
                print "It is not a prime number"

        #for loop to check if num is a square number
        for s in range(0,(num+1)):
                if math.sqrt(num) == s:
                        print "It is a square number"
                        break
        else:
                print "It is not a square number "

        #while loop to check if num is a Fibonacci number
        a,b = 0,1
        while a < num:
                #print a                #print for testing purposes
                a,b = b,a+b

        if a == num:
                print "It is a Fibonacci number"
        else:
                print "It is not a Fibonacci number"

        
                
else:
        print "Maximum allowable value for integer is 2147483647. " + "Please input another number." 
       # num= int(raw_input("Input a number:"))
        
