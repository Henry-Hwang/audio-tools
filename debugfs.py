#!/usr/bin/python3

import os
import sys
import commands
import time
import argparse
import meizu
import tparser
from decimal import Decimal


class debugfs():
	def regs_dump(self, bus):
		os.system("adb shell cat /d/regmap/" + bus +"/registers > regs.txt")
		os.system("subl regs.txt")
	def reg_read(self, bus, reg):
		cmdstr = "adb shell cat /d/regmap/" + bus +"/registers | grep -i " + reg
		result = os.popen(cmdstr)
		ret = result.read()
		print ret
	def reg_write(self, bus, reg, val):
		cmdstr = "adb shell  \"echo " + reg + " " + val + " > /d/regmap/" + bus +"/registers\""
		os.system(cmdstr)