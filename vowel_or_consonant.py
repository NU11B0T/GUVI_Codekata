vowel=['a','e','i','o','u']
print('Enter the char :')
b=raw_input()

try:
    int(b)

except ValueError:
    if len(b) == 1:
        if b in vowel:
            print ('vowel')
        else:
            print ('consonant')
    else:
        print('You have not enter one character')

else:
    print('Only char')

