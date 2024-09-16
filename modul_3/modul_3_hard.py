def calculate_structure_sum(structure):
    total_sum = 0
    for i_structure in structure:
        if isinstance(i_structure, int) or isinstance(i_structure,float):
            total_sum += i_structure
        elif isinstance(i_structure, str):
            total_sum += len(i_structure)
        elif isinstance(i_structure, dict):
            for i, j in i_structure.items():
                total_sum += len(i)
                if isinstance(j, str):
                    total_sum += len(j)
                else:
                    total_sum += j
        else:
            total_sum += calculate_structure_sum(i_structure)
    return total_sum


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)
