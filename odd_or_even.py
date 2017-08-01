print("Enter the number to check even or odd :")
a=raw_input()

try:
    int(a)

except ValueError:
    print ('Not int')

else:
    a=int(a)
    if (a == 0):
        print("Zero")
    elif (a % 2 == 0):
        print("even")
    else:
        print ("odd")
