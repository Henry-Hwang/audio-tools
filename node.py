
# -*- coding: utf-8 -*-
import os
import sys
import commands
import time
import argparse
import tparser
import tinycmd

#节点数据结构
class Dnode(object):
	# 初始化一个节点
	def __init__(self, object = None):
		self.object = object  # 节点值
		self.child_list = []	# 子节点列表
		self.name = object.name

	# 添加一个孩子节点
	def add_child(self, node):
		self.child_list.append(node)

