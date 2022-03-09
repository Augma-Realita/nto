routes = [[4, 3, 0], [2, 1, 0], [8, 7, 6, 0], [5, 6, 0]]


def make_route(start, end):
    isFound = False
    res = []
    for i in range(len(routes)):
        if isFound:
            break
        for j in range(len(routes[i])):
            if routes[i][j] == start:
                for k in range(len(routes[i])):
                    if routes[i][k] == end:
                        if (j < k):
                            tmp = routes[i][j:k]
                            for u in range(len(tmp)):
                                res.append(tmp[u])
                            res.append(routes[i][k])
                        else:
                            tmp = routes[i][k:j]
                            res.append(routes[i][j])
                            for u in range(len(tmp)):
                                res.append(tmp[len(tmp) - u - 1])
                        isFound = True
    if not isFound:

        tmp = make_route(start, 0)
        for u in range(len(tmp)):
            res.append(tmp[u])
        res.remove(0)
        tmp = make_route(0, end)
        for u in range(len(tmp)):
            res.append(tmp[u])

    return res

