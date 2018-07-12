import os
import sys
import commands
import time
import argparse

class halo:
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

class amplifier(object):
	def __init__(self, type, bus, addr, prefix, mixers, rtlog_init, rtlog_get, mute, unmute, temp, cali, load, unload, firmware):
		#print sys._getframe().f_code.co_name
		self.type = type
		self.bus = bus
		self.addr = addr
		self.prefix = prefix
		self.mixers = mixers
		self.mixer_rtlog_init = rtlog_init
		self.mixer_rtlog_get = rtlog_get
		self.mixer_mute = mute
		self.mixer_unmute = unmute
		self.mixer_temp = temp
		self.mixer_cali = cali
		self.mixer_load = load
		self.mixer_unload = unload
		self.mixer_firmware = firmware

	def get_type(self):
		return self.type

	def get_bus(self):
		return self.bus

	def get_addr(self):
		return self.addr

	def get_prefix(self):
		return self.prefix

	def get_mixers(self):
		return self.mixers

	def get_rtlog_init(self):
		return self.mixer_rtlog_init

	def get_rtlog_get(self):
		return self.mixer_rtlog_get

	def get_mute(self):
		return self.mixer_mute

	def get_unmute(self):
		return self.mixer_unmute

	def get_temp(self):
		return self.mixer_temp

	def get_cali(self):
		return self.mixer_cali

	def get_load(self):
		return self.mixer_load

	def get_unload(self):
		return self.mixer_unload

	def get_firmware(self):
		return self.mixer_firmware

	def amp_route(self, path):
		print sys._getframe().f_code.co_name
		return

	def amp_reg_dump():
		print sys._getframe().f_code.co_name

	def amp_reg_set(addr, value):
		print sys._getframe().f_code.co_name

	def amp_reg_get(addr):
		print sys._getframe().f_code.co_name
