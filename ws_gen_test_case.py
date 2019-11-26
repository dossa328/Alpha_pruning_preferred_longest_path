import json
import random
import threading
import alpha_pruning
import cal_all_paths
from Metro2 import Metro

with open('line.json', 'r', encoding='UTF-8') as line_file:
    line_data = json.load(line_file)

with open('input_data.json', 'r', encoding='UTF-8') as data_file:
    input_data = json.load(data_file)

data_set = []

for i in line_data:
    for j in line_data[i]:
        data_set.append(j + i)


def rand_start_end(_data_set):
    while True:
        _start = random.choice(_data_set)
        _end = random.choice(_data_set)

        if _start is not _end:
            break

    return _start, _end


alpha = 1.1
metro = Metro()

# for j in range(888):
#     alpha_pruning.get_result(metro, input_data[str(j)]['from'], input_data[str(j)]['to'], alpha)


def find_all_paths(graph2, start, end, path=[]):
    # global count
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph2:
        return []
    paths = []
    for node in graph2[start]:
        if node not in path:
            newpaths = find_all_paths(graph2, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


time_out = 1
for i in range(10000):
    ran_start, ran_end = rand_start_end(data_set)

    done_counting = threading.Event()
    # t = threading.Thread(target=cal_all_paths.get_result, args=(metro, ran_start, ran_end, alpha))
    t = threading.Thread(target=find_all_paths, args=(metro, ran_start, ran_end))
    t.setDaemon(True)

    t.start()

    t.join(time_out)
    done_counting.wait(time_out)
    # if runtime out (difficult problem)
    if t.is_alive():
        # print("diffi : " ,ran_start, ran_end)
        pass
    # if runtime out (easy problem)
    else:
        print(ran_start, ran_end)
        # pass