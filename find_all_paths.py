
def find_all_paths(graph2, start, end, path=[]):
    global count
    path = path + [start]
    if start == end:
        # if path:
        #     if count % 1000 == 0:
        #         print(count, ":", len(path))
        #     count = count + 1
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