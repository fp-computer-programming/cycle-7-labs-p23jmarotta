# Creator JM 10/9/22

numbers = [] # Define list

print('Please provide three numbers:')

for x in range(0,3): # this one doesn't say no loops!! :)
    numbers.append(int(input())) # add 3 integers to list

numbers_doubled = [numbers[0] * 2, numbers[1] * 2, numbers[2] * 2] # Double each value

print(numbers_doubled) # print result
