import random

def list_numbers():
    list_ = []
    for i_list in range(3, 21):
        list_.append(i_list)
    return list_

def random_numbers(list_ : list):
    num = random.choice(list_)
    return num


list_nums = list_numbers()
# print(list_nums)
random_num = random_numbers(list_nums)
print(f' Число из первой всавки - {random_num}')
result = []

for i in range(1, random_num):
    for j in range(1, random_num):
        if random_num % (i + j) == 0:
            result.append(i)
            result.append(j)


print(*result)
