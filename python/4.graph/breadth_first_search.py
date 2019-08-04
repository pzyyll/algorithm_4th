# -*- coding:utf-8 -*-

from graph import Graph, Search
from collections import deque

class BreadthFirstSearch(Search):
	def __init__(self, g, s):
		'''
		@type g: Graph
		@type s: int
		:param g:
		:param s:
		'''
		super(BreadthFirstSearch, self).__init__(g, s)

		self._marked = [False for _ in range(g.v)]
		self._edgeTo = [-1 for _ in range(g.v)]
		self._s = s
		self.bfs(g, s)

	def bfs(self, g, s):
		queue = deque()
		self._marked[s] = True
		queue.append(s)
		while len(queue):
			v = queue.popleft()
			for w in g.adj(v):
				if not self._marked[w]:
					self._edgeTo[w] = v
					self._marked[w] = True
					queue.append(w)

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
	search = BreadthFirstSearch(g, s)
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
	Test('graph.in', 4)