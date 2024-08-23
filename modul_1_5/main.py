immutable_var = tuple([1, 23, 'string', False, [2, 4, 2, 4]])
print('Immutable tuple:', immutable_var)
print(immutable_var[1])
print(immutable_var[1:])
print(immutable_var[-1][2])
mutable_list = [2, 6, 'text', True]
mutable_list[2] = 'string'
print('Mutable list:', mutable_list)