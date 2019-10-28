# 실험하는 곳임
# 순서는 다음과 같음.
# datasetlist중에서 [ line.json, trans.json, edges_fix json 각각 수정]
# 위에꺼 완료


# gen_test_case.py로 set 만들고 (pairs)
# 나온거를 hwp로 수정하고, 갯수 기록하고
# hwp 수정한다음에
# make_dataset 실행해서
# line 0.0.0_smalldata.json을 얻은다음에
# metro 수정하고, gen_test_case까지 수정한다음
# gen_test_case를 실행하면됨. ;ㅁ;
import json
from Metro import Metro
import gen_test_case

# line input
input_vertex = input().split(',')

fm_trans_json = 'trans_' + ','.join(input_vertex) + '.json'
fm_line_json = 'line_' + ','.join(input_vertex) + '.json'
fm_edges_fix_json = 'edges_fix_' + ','.join(input_vertex) + '.json'

with open('trans.json', 'r', encoding='UTF-8') as json_file:
    trans_data = json.load(json_file)

with open('line.json', 'r', encoding='UTF-8') as line_file:
    line_data = json.load(line_file)

with open('edges_fix.json', 'r', encoding='UTF-8') as edges_fix_file:
    edges_data = json.load(edges_fix_file)

station_to_line = {}
for i in line_data:
    for j in line_data[i]:
        station_to_line[j + i] = i

experiment_trans_data = {}
for j in input_vertex:
    for i in line_data:
        if i in j:
            experiment_trans_data[i] = line_data[i]

# line data 편성
with open(fm_line_json, 'w', encoding="utf-8") as make_file:
    json.dump(experiment_trans_data, make_file, ensure_ascii=False, indent="\t")


same_trans_stations = []
edges_trans_pairs = []
for i in experiment_trans_data:
    for j in experiment_trans_data:
        if i == j:
            pass
        else:
            a = list(set(experiment_trans_data[i]).intersection(experiment_trans_data[j]))
            if a:
                for k in a:
                    edges_trans_pairs.append(["".join(k) + i, "".join(k) + j])
                    b = "".join(k) + i
                    same_trans_stations.extend([b])

same_trans_stations = list(set(same_trans_stations))

# trans 데이터 편성
to_json_same_trans_stations = {}
to_json_same_trans_stations["trans"] = same_trans_stations


with open(fm_trans_json, 'w', encoding="utf-8") as make_file:
    json.dump(to_json_same_trans_stations, make_file, ensure_ascii=False, indent="\t")


# edges_data 편성
edges_small_data = {}
# for i in input_vertex:
#     edges_small_data[i] = edges_data[i]

jn_same_trans_stations = {}
s = []
for i in edges_trans_pairs:
    s.append({"from": i[0], "to": i[1], "distance": 999, "time": 3})

# 완성!
jn_same_trans_stations["Trans"] = s

for i in input_vertex:
    jn_same_trans_stations[i] = edges_data[i]

# 입력!
with open(fm_edges_fix_json, 'w', encoding="utf-8") as make_file:
    json.dump(jn_same_trans_stations, make_file, ensure_ascii=False, indent="\t")

gen_test_case._gen_test(fm_trans_json, fm_line_json, fm_edges_fix_json,input_vertex)
