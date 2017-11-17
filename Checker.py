def check():
    file = open('output_file.txt')
    work_list = file.read().splitlines()
    file.close()

    error_list = []
    for i in work_list:
        if i != '' and i[0] != '#':
            x = i.split(' -> ')
            if int(x[1][-1]) - int(x[0][-1]) != 1:
                error_list.append([i, work_list.index(i)])

    file = open('error_log.txt', 'w')
    if error_list != []:
        for i in error_list:
            file.write('{0} в строке {1}'.format(i[0], i[1]))
    file.close()

