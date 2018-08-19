import os
import sys
import commands
import time
import argparse
import tparser
import tinycmd
from decimal import Decimal
from sndcard import Sndcard

class Asoc(object):
	codecs = []
	dais =[]
	platforms = []
	snd_cards = []
	snd_cards_name = []
	dict_components = {"codecs":codecs, "dais":dais, "platforms":platforms};

	def __init__(self, codec_filter):
			self.codec_filter = codec_filter

	def find_codecs(self):
		f_codecs = []
		cmdstr = "adb shell cat /d/asoc/codecs"
		print cmdstr
		result = os.popen(cmdstr)
		ret = result.read()
		codecs = ret.split('\n')

		for i in range(len(codecs)):
			print codecs[i]
			codecs[i] = codecs[i].strip()

		codecs.remove("")
		if(0 < len(self.codec_filter)):
			for i in range(len(self.codec_filter)):
				if self.codec_filter[i] in codecs:
					f_codecs.append(self.codec_filter[i])
			self.dict_components['codecs'] = f_codecs
		else:
			self.dict_components['codecs'] = codecs
	def get_snd_cards(self):
		cmdstr = "adb shell cat /proc/asound/cards"
		print cmdstr
		result = os.popen(cmdstr)
		ret = result.read()
		snds = ret.split('\n')
		self.snd_cards_name.append(snds[1].strip())
		for i in range(len(self.snd_cards_name)):
			print self.snd_cards_name[i]

	def find_snd_cards(self):
		# just take only one card as default
		self.find_snd_card(self.snd_cards_name[0])

	def find_snd_card(self, card):
		# just take only one card as default
		path = "/d/asoc/" + card
		cmdstr = "adb shell ls" + path
		result = os.popen(cmdstr)
		ret = result.read()
		snds = ret.split('\n')
		if (-1 != ret.find("No such file or directory")):
			print "No such file or directory"
		else:
			print "found " + card
			card = Sndcard(card, path, self.dict_components)
			card.find_codecs()
			#card.find_codec("spi1.0")
			self.snd_cards.append(card)

	def get_codecs(self, sndcard):
		codecs = []
		for i in range(len(self.snd_cards)):
			if(sndcard != self.snd_cards[i].name):
				continue
			#print self.snd_cards[i].name
			codecs = self.snd_cards[i].get_codecs()

		return codecs

	def get_widgets(self, sndcard, codec):
		widgets = []
		for i in range(len(self.snd_cards)):
			if(sndcard != self.snd_cards[i].name):
				continue
			#print self.snd_cards[i].name
			widgets = self.snd_cards[i].get_widgets(codec)

		return widgets

	def get_on_widgets(self, sndcard, codec):
		ons = []
		for i in range(len(self.snd_cards)):
			if(sndcard != self.snd_cards[i].name):
				continue

			ons = self.snd_cards[i].get_on_widgets(codec)
		return ons

	def get_dais(self):
		pass
