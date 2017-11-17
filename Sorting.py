from Checker import check


def sort():
    input_file = open('generated_data.txt')
    work_list = input_file.read().splitlines()
    input_file.close()

    output_file = open('output_file.txt', 'w')

    false_list = []
    first_list = []
    li = []
    for i in work_list:
        if i not in li:
            li.append(i)
        else:
            false_list.append([i, work_list.index(i), len(li)])
    if false_list != []:
        output_file.write('# WARNING!\n# Одинаковые позиции:\n')
        for i in false_list:
            output_file.write('# {0} в строках {1} и {2}\n'.format(i[0][:-2], i[1]+1, i[2]+1))
        output_file.write('# Удалено строк: {}\n\n\n'.format(len(false_list)))
    work_list = li
    work_dict = {}
    leng = len(work_list)
    for i in range(leng):
        type_numb = int(work_list[i][-1])
        work_dict.update({work_list[i]: [type_numb, False, '']})

    for i in range(len(work_list)):
        if (work_dict[work_list[i]][0] == 2 or work_dict[work_list[i]][0] == 3) and work_dict[work_list[i]][1] is False:
            j = i
            if i != 0 and j != 0 and work_dict[work_list[j-1]][1] is False and work_dict[work_list[i]][0] - work_dict[work_list[j-1]][0] == 1:
                while j != 0 and work_dict[work_list[j-1]][1] is False and work_dict[work_list[i]][0] - work_dict[work_list[j-1]][0] == 1:
                    work_dict[work_list[j-1]][1] = True
                    work_dict[work_list[j-1]][2] = work_list[i]
                    j -= 1
                work_dict[work_list[i]][1] = True
            elif i != leng-1 and j != leng-1 and work_dict[work_list[j+1]][1] is False and work_dict[work_list[i]][0] - work_dict[work_list[j+1]][0] == 1:
                while j != leng-1 and work_dict[work_list[j+1]][1] is False and work_dict[work_list[i]][0] - work_dict[work_list[j+1]][0] == 1:
                    work_dict[work_list[j+1]][1] = True
                    work_dict[work_list[j+1]][2] = work_list[i]
                    j += 1
                work_dict[work_list[i]][1] = True
    false_list = []
    for i in range(leng):
        if work_dict[work_list[i]][1] is False:
            false_list.append([work_list[i], i+1+len(set(first_list))])
            work_dict[work_list[i]][2] = 'ERROR'

    if false_list != []:
        output_file.write('# WARNING!\n# Не учтены позиции:\n')
        for i in false_list:
            output_file.write('# {0} в строке {1}\n'.format(i[0], i[1]))
        output_file.write('\n\n')

    for i in work_list:
        if work_dict[i][2] != '':
            output_file.write('{0} -> {1}\n'.format(i, work_dict[i][2]))
    output_file.close()
    check()

