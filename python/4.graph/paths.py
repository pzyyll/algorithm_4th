
from graph import Graph

class Paths(object):
    def __init__(self, graph, s):
        pass

    def hasPathTo(self, v):
        pass

    def pathTo(self, v):
        pass

class DepthFirstPaths(Paths):
    def __init__(self, graph, s):
        super(DepthFirstPaths, self).__init__(graph, s)
        self._marked = []
        self._edgeTo = []
        self._s = s

        self._marked = [False for _ in range(graph.v)]
        self._edgeTo = [0 for _ in range(graph.v)]

        self.dfs(graph, s)

    def dfs(self, g, v):
        self._marked[v] = True
        for w in g.adj(v):
            if not self._marked[w]:
                self._edgeTo[w] = v
                self.dfs(g, w)

    def hasPathTo(self, v):
        return self._marked[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None

        path = []
        x = v
        while x != self._s:
            path.append(x)
            x = self._edgeTo[x]
        path.append(self._s)
        path.reverse()
        return path


def Test(graphCfg, s):
    g = Graph.createFromFile(graphCfg)
    search = DepthFirstPaths(g, s)
    for v in range(g.v):
        print('{} to {}'.format(s, v), end=':')
        if search.hasPathTo(v):
            for x in search.pathTo(v):
                if x == s:
                    print(x, end='')
                else:
                    print('-{}'.format(x), end='')
        print('')

if __name__ == "__main__":
    Test('graph.in', 0)