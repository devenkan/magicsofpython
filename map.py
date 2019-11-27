#map is iterabale object
#it requries function and sequence of input
#map(lambdafunction,sequence)
list_number=[10,20,30,40,50]
list_numbers=map(lambda x:x*10,list_number)
#if we print(list_numbers) it will return map object
#it is iterator so we need to iterate it
for num in list_numbers:
	print(num)


#another example
#if list keyword is already used it shows error

# list = [1, 2, 3]    # remove this list, then it will work.

# def powerof(num):
#     return num**2

# number = [1,2,3,4,5,6,7,8]

# s = list(map( powerof , number))
# print(s)
# #Output :- [1, 4, 9, 16, 25, 36, 49, 64]
