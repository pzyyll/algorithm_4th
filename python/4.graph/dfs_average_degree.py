# -*- coding:utf-8 -*-

import random

from shortest_path import SPNoraml
from graph import Graph

class DFS_ForAverageDegree(object):
	def __init__(self, g, s):
		''' 在图中找到以 s 为起点，间隔度数均等的所有点
		:param g:
		:param s:
		'''

		self._marked = [False for _ in range(g.v)]
		self._points = [s,]
		self._except = set([])
		self._g = g
		self._s = s
		self._sp = SPNoraml(g)
		self._distLimit = (1,2)  # 间隔度数的下限，上限

		self._dfs(g, s)

	def _dfs(self, g, s):
		if s > g.v:
			return

		self._marked[s] = True

		if self._check(s):
			self._addPoint(s)

		adjs = g.adj(s)
		random.shuffle(adjs)
		for v in adjs:
			if not self._marked[v]:
				self._dfs(g, v)

	def _check(self, v):
		limitDist = random.randrange(*self._distLimit)
		if v in self._except:
			return False

		for w in self._points:
			if self._sp.dist(v, w) < limitDist:
				return False

		return self._sp.dist(self._points[-1], v) >= limitDist

	def _addPoint(self, v):
		self._points.append(v)
		self._except.update(self._g.adj(v))

	def getAveragePoints(self):
		return self._points[1:]

if __name__ == '__main__':
	g = Graph.createFromFile('graph4x4.in')
	search = DFS_ForAverageDegree(g, 1)
	print(search.getAveragePoints())