import os
import sys
import commands
import time
import argparse
import tparser
import tinycmd

from decimal import Decimal

class Codec(object):
	name = ""
	def __init__(self):
		pass

	def get_codecs(self):
		cmdstr = "adb shell  cat /d/asoc/codecs"
		print cmdstr
		result = os.popen(cmdstr)
		ret = result.read()
		codecs = ret.split('\n')
		self.codecs = codecs
		#asoc_t = Asoc()
		for i in range(len(codecs)):
			print self.codecs[i]
			#result = os.popen("adb shell cat " + paths[i])
			#ret = result.read()
			#if (ret.strip() != "closed"):
			#	print ret

	def get_snd_cards(self):
		cmdstr = "adb shell  cat /proc/asound/cards"
		print cmdstr
		result = os.popen(cmdstr)
		ret = result.read()
		snds = ret.split('\n')
		self.snd_cards.append(snds[1].strip())
		for i in range(len(self.snd_cards)):
			print self.snd_cards[i]

	def get_dais(self):
		pass
