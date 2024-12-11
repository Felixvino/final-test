# Python program to check if a number is prime or not

num = 407

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2, int(num/8)+1):
       if (num % i) == 0:
           print(num, "is not a prime number")
           break
   else:
       print(num, "is a prime number")
else:
   print(num, "is not a prime number")
