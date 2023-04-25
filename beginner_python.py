#Write a program that asks the user to input a list of integers. The program should do the following:
#Print the total number of items in the list
#Print the last item in the list
#Print the list in reverse order
#Print yes if the list contains a 5 and No otherwise
#Print how many integers in the list are less than 5

def list_maker():
    num_list = input('Enter a list of integers: ')
    num_list = num_list.split(' ')
            
    print(f'There are {len(num_list)} integers in your list')
    print(f'The last item in your list is {num_list[-1]}')
    print(f'Reverse, reverse: {num_list[::-1]}')
    if 5 in num_list:
        print('Yes')
    else:
        print('No')

    count = 0

    for num in num_list:
        if int(num) < 5:
            count += 1

    print(f'There are {count} integers in your list')


# Write a program that gets the user to input a name. The program should:
# Accept a name from the user.
# Check whether the letter 'a' exists in the name.
# If it does, print Yes to the user, if not the program should print No

def name_checker():
    name = input('Enter your name: ').lower()
    if 'a' in name:
        print('Yes')
    else:
        print('No')


# Write a program that repeatedly asks the user to enter 3 product names and prices. The program should do the following:
# Store all of these in a dictionary whose keys are the product names and whose values are the prices.

def product_list_maker():
    shop = {}
    for i in range(3):
        product = input('Enter a product: ')
        price = input(f'Enter the price of {product}: ')
        shop[product] = price
    return shop


# Write a program that asks the user to enter two numbers, x and y, and computes |x-y|/(x+y).

def number_worker():
    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))

    answer = abs(num1-num2)/(num1+num2)

    print(answer)

# Write a program that converts miles to kilometers. The program should:
# Ask  input from the user.
# Check that the input is valid (numeric entry).
# If it is valid, print out the converted distance. If it is invalid, then it prints an error message.

def mi_km_convert():
    try:
        miles = float(input('Enter distance in miles: '))

    except Exception as e:
        print(f'Error: {e}')
    
    km = miles*1.609
    print(f'{miles} miles is equal to {km} km.')


