#!/usr/bin/python3

import os
import sys
import commands
import time
import argparse
import tparser
from decimal import Decimal


class Debugfs():

	def regs_dump(self, bus):
		os.system("adb shell cat /d/regmap/" + bus +"/registers > regs.txt")
		os.system("subl regs.txt")
	def reg_read(self, bus, reg):
		cmdstr = "adb shell cat /d/regmap/" + bus +"/registers | grep -i " + reg
		result = os.popen(cmdstr)
		ret = result.read()
		print ret
	def reg_write(self, bus, reg, val):
		cmdstr = "adb shell \"echo " + reg + " " + val + " > /d/regmap/" + bus +"/registers\""
		os.system(cmdstr)

	def argument(self, parser):
		parser.add_argument("-w", "--write", required=False, help="write [SPK, reg, val]", nargs=3, type=str)
		parser.add_argument("-r", "--read", required=False, help="read [SPK, reg]", nargs=2, type=str)

	def args_send(self, arg):
		if arg.write:
			self.reg_write(arg.write)
		if arg.read:
			self.reg_read(arg.read)