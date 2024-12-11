#Write to check a number is divisible by another number. 

numer=int(input("Enter the numerator."))
denom=int(input("Enter the denominator."))

if numer%denom==0:
    print("\n", numer, "is divisible by ", denom)
else:
    print("\n",numer, "is not divisible",denom)