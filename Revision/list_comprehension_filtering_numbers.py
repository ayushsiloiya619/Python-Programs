numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers_square=[x**2 for x in numbers if x%2==0]
print(even_numbers_square)

numbers=[1,2,3,4,5]
even_numbers=[x for x in numbers if x%2==0]
print(even_numbers)