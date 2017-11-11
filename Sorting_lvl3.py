from pprint import pprint

input_file = open('input_data_lvl3.txt')
work_list = input_file.read().splitlines()
input_file.close()

work_dict = {}
for i in work_list:
    work_dict.update({i: [int(i[-1]), False, '']})
leng = len(work_list)

for i in range(len(work_list)):
    if work_dict[work_list[i]][0] == 2 or work_dict[work_list[i]][0] == 3 and work_dict[work_list[i]][1] is False:
        j = i
        if i != 0 and j != 0 and work_dict[work_list[j-1]][1] is False and work_dict[work_list[i]][0] - work_dict[work_list[j-1]][0] == 1:
            while j != 0 and work_dict[work_list[j-1]][1] is False and work_dict[work_list[i]][0] - work_dict[work_list[j-1]][0] == 1:
                work_dict[work_list[j-1]][1] = True
                work_dict[work_list[j-1]][2] = work_list[i]
                work_dict[work_list[i]][1] = True
                j -= 1

        elif i != leng-1 and j != leng-1 and work_dict[work_list[j+1]][1] is False and work_dict[work_list[i]][0] - work_dict[work_list[j+1]][0] == 1:
            while j != leng-1 and work_dict[work_list[j+1]][1] is False and work_dict[work_list[i]][0] - work_dict[work_list[j+1]][0] == 1:
                work_dict[work_list[j+1]][1] = True
                work_dict[work_list[j+1]][2] = work_list[i]
                work_dict[work_list[i]][1] = True
                j += 1

false_number = 0
for i in work_list:
    if work_dict[i][1] is False:
        false_number += 1
print("Ошибок: ", false_number)
pprint(work_dict)