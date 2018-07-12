import os
import sys
import commands
import time
import argparse
import tinycmd
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
	def __init__(self, type, bus, addr, prefix, mixers, rtlog_init, rtlog_get, mute, unmute, temp, cali, load, unload, firmware, factor, name):
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
		self.factor = factor
		self.name = name
	def cmd_verify(self, cmd, list):
		hit = False
		for i in range(len(list)):
			print list[i]
			if (cmd==list[i]):
				hit = True
				break
		return hit

	# Args:
	# 		cmd: the short command string
	#		list: the full command set, get from tinymix
	# Returns:
	# 		objcmds: list of command object.
	#
	# one 'cmd' can get several full commands, for example:
	# DEBUGMDRXERR -->"SPK DSP1X Protection R cd DEBUGMDRXERR",
	# DEBUGMDRXERR -->"RCV DSP1X Protection L cd DEBUGMDRXERR",

	def get_commands(self, cmd, list):
		str = cmd.split(',')

		if (len(str) > 1):
			strv = str[1].strip()
		objcmds=[]

		for i in range(len(list)):
			if (-1 != list[i].find(str[0])):
				tcmd = tinycmd.tinycmd(list[i], strv)
				objcmds.append(tcmd)

		return objcmds

	# Args:
	# 		cmd: the short command string
	#		list: the full command set, get from tinymix
	# Returns:
	# 		objcmd: command object
	def get_command(self, prefix, cmd, list):
		objcmds = self.get_commands(cmd, list)
		objcmd = objcmds[0]
		for i in range(len(objcmds)):
			#print ltarget[i][0:3]
			cmd_s = objcmds[i].get_cmd()
			if (prefix == cmd_s[0:len(prefix)]):
				objcmd = objcmds[i]
				objcmd.to_command()
				break

		return objcmd

	# Args:
	# 		cmds: the short command string list to be executed
	#		list: the full command set, get from tinymix
	# Returns:
	# 		objcmd: list of command object
	def get_bulk_command(self, prefix, cmds, list):
		objcmds = []
		for i in range(len(cmds)):
			objcmds.append(self.get_command(prefix, cmds[i], list))
		return objcmds

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
