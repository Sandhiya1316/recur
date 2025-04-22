def factorial(n):
n =input("please enter you number")
if n==0:
return 1
else:
return n*factorial(n-1)
print (factorial(n))