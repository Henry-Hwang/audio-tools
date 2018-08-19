import os
import sys
import commands
import time
import argparse
import tparser
import tinycmd

from decimal import Decimal


class Widget(object):
	name = "None"
	state= "None"
	n_ins_name="None"
	n_outs_name="None"
	values="None"
	mask="None"
	ins_name = []
	outs_name = []
	'''
	/d/asoc/sdm845-tavil-snd-card/codec:spi1.0/dapm/SPK\ ASPRX1
	SPK ASPRX1: On in 1 out 6 - R18432(0x4800) mask 0x10000
	out "static" "SPK VBSTMON ADC"
	out "static" "SPK TEMPMON ADC"
	out "static" "SPK VPMON ADC"
	out "static" "SPK IMON ADC"
	out "static" "SPK VMON ADC"
	out "static" "SPK DSP1"
	in "static" "SPK AMP Enable"
	'''
	def __init__(self, path, status):
		self.path = path
		self.status = status
		self.ins_name = []
		self.outs_name = []

	def init(self):
		#get name of widget
		#status_lines = self.status.split("\n")
		#status_lines.remove("")
		lines = self.status[0].split(":")
		self.name = lines[0].strip()

		#print self.status

		if(len(lines) < 2):
			return

		# parser status
		st = lines[1].strip().split(" ")
		self.state = st[0]

		# get ins_name number
		pos = st.index("in")
		self.n_ins_name = st[pos + 1]

		# get outs_name number
		pos = st.index("out")
		self.n_outs_name = st[pos + 1]

		# get register/value & mask
		if "-" in st:
			pos = st.index("-")
			self.values = st[pos + 1]

			pos = st.index("mask")
			self.mask = st[pos + 1]

		#print self.state, self.n_ins_name, self.n_outs_name, self.values, self.mask

		# skip first line
		for i in range(1, len(self.status)):
			self.status[i] = self.status[i].strip()
			if ("out" == self.status[i][0:len("out")]):
				self.outs_name.append(self.status[i].replace("out","").replace("static","").replace("\"\"","").strip())

			elif ("in" == self.status[i][0:len("in")]):
				self.ins_name.append(self.status[i].replace("in", "").replace("static","").replace("\"\"","").strip())

		#for i in range(len(self.outs_name)):
		#	print self.outs_name[i]

		#for i in range(len(self.ins_name)):
 		#	print self.ins_name[i]

	def get_reg(self):
		return self.reg

	def get_state(self):
		return self.state

	def get_ins_name(self):
		return self.ins_name

	def get_outs_name(self):
		return self.outs_name

	# Get out widgets in the list
	def get_outs(self, widgets):
		outs = []
		for i in range(len(widgets)):
			for j in range(len(self.outs_name)):
				if (-1 != self.outs_name[j].find(widgets[i].name)):
					outs.append(widgets[i])
					break
		return outs

	def show(self):
		print self.name, self.state
		print self.ins_name
		print self.outs_name



