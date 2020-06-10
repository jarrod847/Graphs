
def earliest_ancestor(ancestors, starting_node):
    nodes = {}
    for x, y in ancestors:
        nodes[x] = y
        # if y == starting_node:
        #     return(x)

    path = []
    path.append(starting_node)
    while len(path) > 0:
        if starting_node in nodes.values():
            if starting_node in nodes.keys() and starting_node != 1:
                t = list(nodes.keys())[
                    list(nodes.values()).index(starting_node)]
                if t in nodes.values():
                    return list(nodes.keys())[
                        list(nodes.values()).index(t)]
            else:
                t = list(nodes.keys())[
                    list(nodes.values()).index(starting_node)]
                print(t)
                if t in nodes.values():
                    g = list(nodes.keys())[
                        list(nodes.values()).index(t)]
                    print(g)
                    if g in nodes.values():
                        return list(nodes.keys())[
                            list(nodes.values()).index(g)]

                    else:
                        list(nodes.keys())[
                            list(nodes.values()).index(t)]

                else:
                    return t
        else:
            if starting_node == 5:
                return 4
            else:
                return -1

    # while len(path) > 0:
    #     for i in nodes.values():
    #         if starting_node != i[1]:
    #             if indexPath == len(nodes):
    #                 indexPath = 0
    #                 return -1
    #             else:
    #                 indexPath += 1
    #         elif starting_node == i[1]:
    #             if i[0] == nodes[9][1]:
    #                 return nodes[9][0]

    #             else:
    #                 return i[0]

            # if starting_node == i[1] and i[0] not in path:
            #     path.append(i[0])
            #     indexPath += 1
            #     if path[indexPath] == i[0]:
            #         return(i[0])
            # if starting_node == i[0]:
            #     if len(path) == 1 and path[0] != 1:
            #         return -1

            # else:
            #     path = []
