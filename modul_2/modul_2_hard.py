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
random_num = random_numbers(list_nums)
print(f' Число из первой всавки - {random_num}')
result = []
new_result = []
for i in range(1, random_num):
    for j in range(1, random_num):
        if random_num % (i + j) == 0 and i != j:
            flag = True
            for i_result in result:
                if i in i_result and j in i_result:
                    flag = False
            if flag:
                result.append([i, j])
for i_result in result:
    for j_result in i_result:
        new_result.append(j_result)
print(*new_result)
