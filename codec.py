import os
import sys
import commands
import time
import argparse
import tparser
import tinycmd

from decimal import Decimal
from widget import Widget

class Codec(object):
	path = ""
	name = ""
	widgets = []
	dsps = []

	def __init__(self, name, path):
		self.name = name
		self.path = path
		self.widgets=[]
		pass

	def find_widgets(self):
		cmdstr = "adb shell find " + self.path + "/dapm" + " -maxdepth 1"
		#print cmdstr
		result = os.popen(cmdstr)
		ret = result.read()
		lines = ret.split('\n')
		#self.codecs = codecs
		for i in range(len(lines)):
			# widget name with space, so need '\' to convert
			lines[i] = lines[i].replace(" ", r"\ ")

			# skip bias_level in directory
			if (-1 != lines[i].find("bias_level")):
				continue

			#print lines[i]

			#cat the status of widgets
			'''
			/d/asoc/sdm845-tavil-snd-card/codec:spi1.0/dapm/SPK\ ASPRX1
			SPK ASPRX1: On  in 1 out 6 - R18432(0x4800) mask 0x10000
			out  "static" "SPK VBSTMON ADC"
			out  "static" "SPK TEMPMON ADC"
			out  "static" "SPK VPMON ADC"
			out  "static" "SPK IMON ADC"
			out  "static" "SPK VMON ADC"
			out  "static" "SPK DSP1"
			in  "static" "SPK AMP Enable"
			'''
			cmdstr = "adb shell cat " + lines[i]
			result = os.popen(cmdstr)
			ret = result.read()
			winfo = ret.split('\n')
			w = Widget(lines[i], winfo)
			w.init()
			#print "Add  " + w.name + "   to " + self.name
			self.widgets.append(w)
		#print self
		#print "=============" + self.name
		#for i in range(len(self.widgets)):
		#	print self.widgets[i].name

	def get_on_widgets(self):
		ons = []
		#print "Find on widgets for " + self.name
		for i in range(len(self.widgets)):
			if ("On" == self.widgets[i].state):
				ons.append(self.widgets[i])
		return ons

	def find_dsps(self):
		pass

	def find_dais(self):
		pass

	def get_widgets(self):
		#for i in range(len(self.widgets)):
		#	print self.widgets[i].name

		return self.widgets

	def get_dsps(self):
		pass

	def get_dais(self):
		pass
