from test import ParseGraphVertexEdge

class Graph(object):
    def __init__(self):
        self.v = 0
        self.e = 0
        self._adj = []

    def setV(self, v):
        self.v = v
        self.e = 0

        self._adj = [[] for _ in range(self.v)]

    def addEdge(self, v, w):
        if v > self.v or w > self.v:
            return

        if w in self._adj[v]:
            return

        self._adj[v].append(w)
        self._adj[w].append(v)
        self.e += 1

    def adj(self, v):
        if v > self.v:
            raise Exception('limit v')
        return self._adj[v]

    def toString(self):
        res = ''
        for i, listV in enumerate(self._adj):
            res += '%d: '%i
            for v in listV:
                res += str(v)
                if v is not listV[-1]:
                    res += '->'
            res += '\n'
        return res

    @staticmethod
    def createFromFile(file):
        v, edges = ParseGraphVertexEdge(file)
        g = Graph()
        g.setV(v)
        for e in edges:
            g.addEdge(e[0], e[1])
        return g

class Search(object):
    def __init__(self, g, s):
        """
        @type g: Graph
        :param g:
        :param s:
        """
        pass
    
    def marked(self, v):
        pass

    def count(self):
        pass

