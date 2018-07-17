import os
import sys
import commands
import time
import argparse
import tparser
import tinycmd

from decimal import Decimal
from codec import Codec

class Sndcard(object):
	codecs = []
	snd_cards = []
	path=""
	def __init__(self, name, path, dict_components):
		self.name = name
		self.path = path
		self.dict_components = dict_components
		pass

	def find_codec(self, name):
		cmdstr = "adb shell find " + self.path + " -maxdepth 1"
		#print cmdstr
		result = os.popen(cmdstr)
		ret = result.read()
		lines = ret.split('\n')
		#self.codecs = codecs
		for i in range(len(lines)):
			if(-1 != lines[i].find(name)):
				#print lines[i]
				codec = Codec(name, lines[i])
				codec.find_widgets()
				#print codec
				self.codecs.append(codec)

	def find_codecs(self):
		codecs = self.dict_components['codecs']
		#print len(codecs)
		for i in range(len(codecs)):
			#print codecs
			self.find_codec(codecs[i])

	def get_dais(self):
		pass

	def get_codecs(self):
		return self.codecs

	def get_widgets(self, codec):
		widgets = []
		for i in range(len(self.codecs)):
			if(codec == self.codecs[i].name):
				print self.codecs[i].name
				widgets = self.codecs[i].get_widgets()
				break

		return widgets

	def get_on_widgets(self, codec):
		ons = []
		for i in range(len(self.codecs)):
			if(codec != self.codecs[i].name):
				continue

			print self.codecs[i].name
			ons = self.codecs[i].get_on_widgets()

		return ons

