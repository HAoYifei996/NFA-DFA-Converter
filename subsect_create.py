''' this program is for NFA --> DFA
    NFA is saved as a directed graph and need manually input the graph to the graph
'''


class Graph():
    node_num = 0
    edges=[]

    def __init__(self, node_num):
        self.node_num = node_num
        for _ in range(node_num):
            self.edges.append([])

    def get_edge(self, start, end):
        for edge in self.edges[start]:
            if edge[0] == end:
                return edge[1]
        return 0 # 0 means no edge between start and end

    def get_end(self, start, val):
        ans = []
        for edge in self.edges[start]:
            if edge[1] is val:
                ans.append(edge[0])
        return ans

    def add_edge(self, start, end, value):
        self.edges[start].append([end, value])

''' Your Graph initialization goes here

graph = Graph(11)
graph.add_edge(0, 7, 'e')
graph.add_edge(0, 1, 'e')
graph.add_edge(1, 2, 'e')
graph.add_edge(1, 4, 'e')
graph.add_edge(2, 3, 'a')
graph.add_edge(4, 5, 'b')
graph.add_edge(3, 6, 'e')
graph.add_edge(5, 6, 'e')
graph.add_edge(6, 7, 'e')
graph.add_edge(7, 8, 'a')
graph.add_edge(8, 9, 'a')
graph.add_edge(8, 9, 'b')
graph.add_edge(9, 10, 'a')
graph.add_edge(9, 10, 'b')
graph.add_edge(6, 1, 'e')

Uncomment this demo graph if you want to use it'''

def get_key(dic, val):
	return [k for k, v in dic.items() if v == val]

def move(graph, T, val):
    ans = []
    for node in T:
        ans += graph.get_end(node, val)
    return ans

def eps_cover(grpah, T):
    ans = []
    for node in T:
        ans.append(node)
    for node in T:
        next_eps = graph.get_end(node, 'e')
        for nodee in next_eps:
            if nodee not in ans:
                ans.append(nodee)
        for nodeee in eps_cover(graph, next_eps):
            if nodeee not in ans:
                ans.append(nodeee)
    ans.sort()
    return ans


if __name__ == '__main__': # start convert
    new_set = []
    state_name = {}
    wait = []
    wait.append(eps_cover(graph, [0]))
    name = 65
    while(wait):
        curr_state = wait[0] # current processing state
        a = eps_cover(graph, move(graph, curr_state, 'a'))
        b = eps_cover(graph, move(graph, curr_state, 'b'))

        new_set.append([curr_state, a, b])
        state_name[chr(name)] = curr_state
        name += 1

        flag_a = 0
        flag_b = 0

        for elt in new_set: # if a or b haven't been processed, need to be processed
            if elt[0] == a:
                flag_a = 1
            if elt[0] == b:
                flag_b = 1
            if flag_a and flag_b:
                break
        if not flag_a and a not in wait:
            wait.append(a)
        if not flag_b and b not in wait:
            wait.append(b)

        wait.pop(0)

    name = 65
    for row in new_set:
    	print(chr(name) + ': ' + str(row[0]))
    	name += 1

    print('\n\n')

    for row in new_set:
    	print(str(get_key(state_name, row[0])) + ': ' + str(get_key(state_name, row[1])) + ', ' + str(get_key(state_name, row[2])))

























