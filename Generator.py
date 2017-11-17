import random as rnd

from Sorting import sort


def gen():
    max_len = 200
    gen_list = []
    counter = [0, 0, 0]
    name = ['Pachka#', 'Korobka#', 'Palleta#']
    quantity = [3, 10]
    last_type = ''
    last_direct = ''

    while len(gen_list) <= max_len:
        app_list = []
        cur_type = rnd.randint(0, 1)
        cur_direct = rnd.randint(0, 1)
        if cur_type == 0 and last_type == 1 and last_direct == 1:
            cur_direct == 0
        elif cur_type == 1 and last_type == 0 and last_direct == 0:
            cur_direct == 1
        elif last_type == cur_type and last_direct == 1 and cur_direct == 0:
            cur_direct = 1
        if cur_direct == 0:
            for x in range(rnd.randint(1, quantity[cur_type])):
                app_list.append(name[cur_type] + str(x+counter[cur_type]) + '_' + str(cur_type+1))
            counter[cur_type] += len(app_list)
            app_list.append(name[cur_type+1] + str(counter[cur_type+1]) + '_' + str(cur_type+2))
            counter[cur_type+1] += 1
        else:
            app_list.append(name[cur_type + 1] + str(counter[cur_type + 1]) + '_' + str(cur_type + 2))
            counter[cur_type + 1] += 1
            for x in range(rnd.randint(1, quantity[cur_type])):
                app_list.append(name[cur_type] + str(x+counter[cur_type]) + '_' + str(cur_type+1))
            counter[cur_type] += len(app_list)-1
        gen_list.extend(app_list)
        last_type = cur_type
        last_direct = cur_direct
    file = open('generated_data.txt', 'w')
    for i in gen_list:
        file.write(i+'\n')
    file.close()
    sort()


gen()
