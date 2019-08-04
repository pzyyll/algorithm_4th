# -*- coding:utf-8 -*-

from graph import Graph, Search
from breadth_first_search import BreadthFirstSearch

class SP(BreadthFirstSearch):
	def __init__(self, g, s):
		'''
		@type g: Graph
		:param g:
		:param s:
		'''
		super(SP, self).__init__(g, s)
		self._distTo = [-1 for _ in range(g.v)]

	def distTo(self, v):
		if not self.hasPathTo(v):
			return -1

		if self._distTo[v] < 0:
			sortestPath = self.pathTo(v)
			self._distTo[v] = len(sortestPath) - 1
			print('{}->{}'.format(self._s, v), sortestPath)
		return self._distTo[v]

class SPNoraml(object):
	def __init__(self, g):
		'''
		@type g: Graph
		:param g:
		'''
		self._g = g
		self._sps = [SP(g, s) for s in range(self._g.v)]

	def dist(self, s, v):
		if not self.hasPath(s, v):
			return -1
		return self._sps[s].distTo(v)

	def path(self, s, v):
		if not self.hasPath(s, v):
			return None
		return self._sps[s].pathTo(v)

	def hasPath(self, s, v):
		return self._sps[s].hasPathTo(v)

def Test(graphCfg, s):
	g = Graph.createFromFile(graphCfg)
	search = SP(g, s)
	for v in range(g.v):
		print('{} to {}'.format(s, v), end=':')
		if search.hasPathTo(v):
			for x in search.pathTo(v):
				if x == s:
					print(x, end='')
				else:
					print('-{}'.format(x), end='')
		print('')

def TestDist(graphCfg, s, v):
	g = Graph.createFromFile(graphCfg)
	search = SP(g, s)
	print('{}->{} dist: {}'.format(s, v, search.distTo(v)))

if __name__ == '__main__':
    Test('graph.in', 4)
    TestDist('graph.in', 4, 6)

    g = Graph.createFromFile('graph4x4.in')
    sp = SPNoraml(g)

    testCase = ((1,2),(0,8),(2,6),(4,8),(0,15),(0,5),(0,14),(9,8),(8,9),(6,12))
    for case in testCase:
	    print('')
	    print('{}->{} dist: {}'.format(case[0], case[1], sp.dist(case[0], case[1])))