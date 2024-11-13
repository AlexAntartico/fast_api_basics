count = 5
print(type(count))
# <class 'int'>  

count_a = '5'
print(type(count_a))
# <class 'str'>  


def get_total(price1, price2):
    return price1+price2

print(get_total(200, 90))
# print(get_total(count, 90)) 
# TypeError: can only concatenate str (not "int") to str


def total_string(price_1,price_2):
    return f'Your total bill is USD: {price_1+price_2}'


# Print result as string
print(total_string('200', '90'))


def total_hinted(price_1:int,price_2:int)->str:
    '''
    Hinting also makes IDEs better at understanding the identifier types
    Autocomplete will work better and you will get better suggestions

    Fewer bugs
    '''
    return f'Your total bill is USD: {price_1+price_2}'

# expected result
price = total_hinted(200, 90)

# hints dont meant Python is statically typed, interpreter will not
# enforce type annotations
print(price)