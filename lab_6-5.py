# Creator JM 10/9/22

user_list = [1,2,3,4,5,6,7,8,9,0]

user_list.sort()

if len(user_list) <= 2 or user_list[-1] == user_list[0]:
    print('error: list does not meet specifications')
else:
    print(f'Highest: {user_list[-1]}, lowest: {user_list[0]}')