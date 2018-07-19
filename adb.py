import os
import sys
import commands
import time
import argparse
import m1882
import rtlog

import tparser
from decimal import Decimal
class Adb(object):

	def argument(self, parser):
		parser.add_argument("-ai", "--adb", required=False, help="adb init", type=str)
		parser.add_argument("-ap", "--adb-push", required=False, help="adb push", nargs=2, type=str)
		parser.add_argument("-wi", "--wisce-init", required=False, help="adb push", type=str)
		parser.add_argument("-de", "--debug", required=False, help="debug", type=str)

	def init(self, op):
		os.system("adb wait-for-device")
		os.system("adb root")
		os.system("adb wait-for-device")
		os.system("adb remount")
		os.system("adb wait-for-device")
		os.system("adb shell setenforce 0")


	def push(self, op):
		os.system("adb push " + op[0] + " " + op[1])

	def dmesg_loop(self, op):
		if op != "N":
			CMDSTR = "adb shell dmesg -c | grep -iE " + op
		else:
			CMDSTR = "adb shell dmesg -c "
		print CMDSTR
		while True:
			os.system(CMDSTR)
	def wisce_init(self, op):
		os.system("adb forward tcp:22349 tcp:22349")
		os.system("adb shell")
	def dmesg_dump(self, op):
		pass
	def logcat_dump(self, op):
		pass

	def args_send(self, arg):
		if arg.dmesg_loop:
			self.dmesg_loop(arg.dmesg_loop)
		if arg.adb:
			self.adb(arg.adb)
		if arg.adb_push:
			self.adb_push(arg.adb_push)
		if arg.wisce_init:
			self.wisce_init(arg.wisce_init)
