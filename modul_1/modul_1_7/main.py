grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
student = {'Johnny', 'Bilbo', 'Steven', 'Khendrik', 'Aaron'}
for i in range(len(grades)):
    grades[i] = sum(grades[i])/ len(grades[i])
print(grades)
list_student = list(student)
list_student.sort()
print(list_student)
dict_student = dict()
for i in range(len(list_student)):
    dict_student[list_student[i]] = grades[i]
print(dict_student)
