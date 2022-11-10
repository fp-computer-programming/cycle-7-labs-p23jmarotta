# Creator JM 10/9/22

one = int(input('1st number: '))
two = int(input('2nd number: ')) # Define three words
three = int(input('3rd number: '))
numbers = [one, two, three] # Put them in a list

# Check if they are odd or even using modulus 2
if one % 2 == 0 and two % 2 == 0 and three % 2 == 0: # This would be a great place for a loop
    print('even')
elif one % 2 == 1 and two % 2 == 1 and three % 2 == 1:
    print('odd')
else: # If they aren't all even or odd they must be mixed
    print('mixed')