import os
import sys
import commands
import time
import argparse
import tinycmd
import tparser


class Halo:
	def dsp_reinit(self, cmd):
		print sys._getframe().f_code.co_name
		return
	#def dsp_mute(self, cmd):
	#	print sys._getframe().f_code.co_name
	#	return

	def dsp_commands(self, list):
		print sys._getframe().f_code.co_name
		for i in range(len(list)):
			print list[i]
			os.system(list[i])
		return

	def dsp_command(self, cmd):
		os.system(cmd)
		return

	def dsp_get_command(self, cmd):
		#print sys._getframe().f_code.co_name
		string = os.popen(cmd)
		ret = string.read()
		#print ret
		return ret

	def dsp_rt_show(self, count):
		print count
	def dsp_reg_dump():
		print sys._getframe().f_code.co_name
	def dsp_reg_set(self, addr, value):
		print sys._getframe().f_code.co_name
	def dsp_reg_get(self, addr):
		print sys._getframe().f_code.co_name
		return
	def dsp_rtlog_init(self, list):
		print sys._getframe().f_code.co_name
		for i in range(len(list)):
			print list[i]
			os.system(list[i])
		return

