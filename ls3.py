# Отсортируйте словарь по значению в порядке возрастания и убывания.
# Импортируем нужный модуль и объявляем словарь:
import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Сортируем в порядке возрастания:
result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(result)
print(" ")
# И в порядке убывания:
new_result = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(new_result)
print(" ")
# Моё решение в порядке возрастания
my_dict = {"петя": 1234, "jkl": 987, "bvnm": 987, "sdhjh": 6578, "sdgfs": 123}
for i in sorted(my_dict.items(), key=lambda para: para[1], ):
    print(i)
print(" ")
# Моё решение в порядке убывания
my_dict = {"петя": 1234, "jkl": 987, "bvnm": 987, "sdhjh": 6578, "sdgfs": 123}
for i in sorted(my_dict.items(), key=lambda para: para[1], reverse=True):
    print(i)
