print("Enter the number to check positive or negative :")
a=raw_input()
try:
    int(a)

except ValueError:
    print ('Not int')

else:
    a=int(a)
    if (a == 0):
        print("Zero")
    elif (a > 0):
        print("positive")
    else:
        print ("negative")
