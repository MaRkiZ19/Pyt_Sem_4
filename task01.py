# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

string_1="a a a b c a a d c d d".split()
# my_dict={}
# string_out=""
# for i in range(len(string_1)):
#     if string_1[i] not in my_dict.keys():
#         my_dict[string_1[i]] = 1
#         string_out+=f'{string_1[i]} '
#     else :
#         string_out+=f'{string_1[i]}_{my_dict[string_1[i]]} '
#         my_dict[string_1[i]]+=1
# print(string_out)

result=""
for j in range(len(string_1)):
    if string_1[0:j:].count(string_1[j]) == 0:
        result+=f'{string_1[j]} '
    else:
        result+=f' {string_1[j]}_{string_1[0:j:].count(string_1[j])} '
print(result)