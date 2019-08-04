from graph import Graph, Search

class DepthFirstSearch(Search):
    def __init__(self, g, s):
        super(DepthFirstSearch, self).__init__(g, s)
        self._marked = [False for _ in range(g.v + 1)]
        self._count = 0

        self.dfs(g, s)

    def dfs(self, g, v):
        self._marked[v] = True
        self._count += 1
        for w in g.adj(v):
            if not self._marked[w] :
                self.dfs(g, w)

    def marked(self, v):
        return self._marked[v]

    def count(self):
        return self._count

def TestSearch(s):
    g = Graph.createFromFile('graph.in')
    search = DepthFirstSearch(g, s)
    for v in range(0, 10):
        if search.marked(v):
            print(str(v) + ' ', end='')
    print('')
    if search.count() != g.v:
        print('Not ', end='')
    print('connected')

if __name__ == '__main__':
    TestSearch(1)