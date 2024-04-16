# Выведите все элементы, которые меньше 5.
const = 5

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in my_list:
    if i < const:
        print(i)
print(list(filter(lambda elem: elem < const,my_list )))

print([elem for elem in my_list if elem < const])
