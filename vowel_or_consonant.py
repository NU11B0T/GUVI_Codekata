vowel=['a','e','i','o','u']
print('Enter the char :')
b=str(raw_input())
if  len(b)==1:
    if b in vowel:
        print ('vowel')
    else:
        print ('consonant')
else:
    print('You have not enter one character')


