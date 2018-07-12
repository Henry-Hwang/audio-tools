import os
import sys
import commands
import time
import argparse
import csdevs
from decimal import Decimal
class parser():
	# RCV DSP1X Protection L cd CSPL_COMMAND
	# convert 32bit string to int
	# '01 02 0A 0B' --> 0x01020A0B
	def n1_32bit_str(self, string):
		int32 = string.split(':')[1]
		int32=int32.strip()
		int32 = int32.replace(' ','')
		int32 = int(int32, 16)
		return int32

	# convert String to int list
	#  '00  00  2b  94  00  00  2b  fb  00  17  6d  b7  00  17  6d  b7'
	#  --> 0x00002b94, 0x00002bfb, 0x00176db7, 0x00176db7
	def n4_32bit_str(self, str):
		log = str.split(':')[1]
		log=log.strip()
		log = log.replace(' ','')
		_1st = int(log[0:8], 16)
		_2nd = int(log[8:16], 16)
		_3rd = int(log[16:24], 16)
		_4th = int(log[24:32], 16)
		#Q10.13, @5.18
		return (_1st, _2nd, _3rd, _4th)

	def to_decimal(self, val, _int, _dec):
		return Decimal(1.0 * val/(1 << _dec))
