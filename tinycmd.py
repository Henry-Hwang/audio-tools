import os
import sys
import commands
import time
import argparse
import csdevs
import tparser

from decimal import Decimal

class tinycmd():
	shell = "adb shell "
	tinymix = "tinymix "
	command = ""
	value = ""
	execmd = ""
	def __init__(self, cmd, val):
		self.command = cmd
		self.value = val

	def get_cmd(self):
		return self.command

	def set_cmd(self, cmd):
		self.command = cmd

	def get_val(self):
		return self.value

	def set_val(self, val):
		self.value = val

	def to_command(self):
		self.execmd = self.shell + '"' + self.tinymix + "'" + self.command + "' " + self.value + '"'
		return self.execmd

	def exe_command(self):
		#print self.execmd
		os.system(self.execmd)

	def exe_get_command(self):
		result = os.popen(self.execmd)
		ret = result.read()
		#print ret
		return ret
