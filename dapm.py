#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import commands
import time
import argparse
import tparser
import tinycmd
import copy

from decimal import Decimal
from widget import Widget
from dpath import Dpath
from node import Dnode

class Dapm(object):
	dpaths = []
	widgets = []

	def __init__(self):
		# without init will cause memery over write
		self.dpaths = []
		self.widgets = []

	def add_widget(self, widget):
		#print "Add: " + widget.show()
		self.widgets.append(widget)

	def add_widgets(self, widgets):
		self.widgets.extend(widgets)

	def show_path(self, path):
		str = []

		for n in path:
			str.append(n.name)

		print "-->".join(str)

	def search_out(self, nodes = [], widgets=[], result=[]):
		for i in range(len(nodes)):
			outs_t = nodes[i].object.get_outs(widgets)
			if outs_t == []:
				break
			else:
				for j in range(len(outs_t)):
					nodes[i].add_child(Dnode(outs_t[j]))
					print "Add Child: " + outs_t[j].name
				self.search_out(nodes[i].child_list, widgets, result)

		return 'end'

	# 深度优先查找 返回从根节点到目标节点的路径
	def deep_first_search(self, node, name, path=[]):
		#print node
		path.append(node.object) # 当前节点值添加路径列表

		if node.object.name == name:	# 如果找到目标 返回路径列表
			self.show_path(path)
			return path

		if node.child_list == []:	# 如果没有孩子列表 就 返回 no 回溯标记
			return 'no'

		for n in node.child_list: # 对孩子列表里的每个孩子 进行递归
			t_path = copy.deepcopy(path)	# 深拷贝当前路径列表
			self.show_path(t_path)

			res = self.deep_first_search(n, name, t_path)

			if res == 'no': # 如果返回no，说明找到头 没找到 利用临时路径继续找下一个孩子节点
				continue
			else :
				return res # 如果返回的不是no 说明 找到了路径

		return 'no' # 如果所有孩子都没找到 则 回溯

	# 获取最短路径 传入两个节点值，返回结果

	def get_shortest_path(self, root, start_name, end_name):
		# 分别获取 从根节点 到start 和end 的路径列表，如果没有目标节点 就返回no

		#print root
		path1 = self.deep_first_search(root, start_name, [])
		path2 = self.deep_first_search(root, end_name, [])

		if path1 == 'no' or path2 == 'no':
			return '无穷大','无节点'

		# 对两个路径 从尾巴开始向头 找到最近的公共根节点，合并根节点
		len1,len2 = len(path1),len(path2)

		for i in range(len1 - 1, -1, -1):
			if path1[i] in path2:
				index = path2.index(path1[i])
				path2 = path2[index:]
				path1 = path1[-1:i:-1]
				break

		res = path1 + path2
		length = len(res)

		self.show_path(res)

	def create_multiway_tree(self):
		print "create_multiway_tree"
		dpath = Dpath()
		root = []
		w = ""
		# get start point
		for i in range(len(self.widgets)):
			if (-1 != self.widgets[i].name.find("Playback")):
				#print self.widgets[i].name
				w = self.widgets[i]
				dpath.add_widget(w)
				break

		if w == "":
			print "No widgets, may be no DAPM path connected"
			return

		outs = w.get_outs(self.widgets)

		#for i in range(len(outs)):
		#	print outs[i].name

		root.append(Dnode(w))
		self.search_out(root, self.widgets, result=[])
		self.get_shortest_path(root[0], "SPK AMP Playback", "SPK Main AMP")


