def print_params(a= 1, b= 'строчка', c= True):
    print(a, b, c)


#1
#print_params()
#print_params(123)
#print_params(123, 'другая строчка')
#print_params(b= 25)
#print_params(c= [1, 2, 3])

#2
# value_list = [1, 'буквы', (1, 2, 3)]
# values_dict = {'a': 2, 'b': 'string', 'c': [1, 2, 3]}
# print_params(*value_list)
# print_params(**values_dict)

#3
values_list_2 = [5, 'strings']
print_params(*values_list_2, 42)
