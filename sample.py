def factorial(n):
n =input("please enter you number")
if n==0:
return 1
elif n<0:
    print(" Factorial is not valid for Negative Numbers")
else:
return n*factorial(n-1)
print (factorial(n))