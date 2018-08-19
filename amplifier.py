import os
import sys
import commands
import time
import argparse
import tinycmd
import tparser
from decimal import Decimal
from tinycmd import Tinycmd
from tparser import Tparser


class Amplifier(object):
	def __init__(self, type, bus, addr, prefix, firmware, factor, name, dict_mixers):
		#print sys._getframe().f_code.co_name
		self.type = type
		self.bus = bus
		self.addr = addr
		self.prefix = prefix
		self.mixer_firmware = firmware
		self.factor = factor
		self.name = name
		self.dict_mixers = dict_mixers

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
				tcmd = tinycmd.Tinycmd(list[i], strv)
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

	def get_factor(self):
		return self.factor



	def get_prot(self, result, temp_h):
		parser = Tparser()
		temp = parser.n1_32bit_str(temp_h)
		z_min, z_max, factor_min, factor_max = parser.n4_32bit_str(result)
		temp = parser.to_decimal(temp, 9, 14)
		z_min = parser.to_decimal(z_min, 10, 13)
		z_max = parser.to_decimal(z_max, 10, 13)
		factor_min = parser.to_decimal(factor_min, 5, 18)
		factor_max = parser.to_decimal(factor_max, 5, 18)

		return z_min, z_max, temp, factor_max
	def show_prot(self):
		objcmds = self.get_bulk_command(self.prefix, self.dict_mixers['rtlog_init'], self.dict_mixers['mixers'])
		for i in range(len(objcmds)):
			objcmds[i].exe_command()

		print "----------------------------------------"
		for i in range(100):
			objcmd = self.get_command(self.prefix, self.dict_mixers['dsp_temp'][0], self.dict_mixers['mixers'])
			temp = objcmd.exe_get_command()

			objcmd = self.get_command(self.prefix, self.dict_mixers['rtlog_get'][0], self.dict_mixers['mixers'])
			result = objcmd.exe_get_command()
			z_min, z_max, temp, factor_max = self.get_prot(result, temp)
			z_min = z_min * Decimal(self.factor)
			z_max = z_max * Decimal(self.factor)

			print "(%3.2f" % z_min, " %3.2f )ohm" % z_max, " T (%3.2f)" %temp


	def dsp_load(self):
		objcmd = self.get_command(self.prefix, self.mixer_firmware[0], self.dict_mixers['mixers'])
		objcmd.exe_command()

		objcmds = self.get_bulk_command(self.prefix, self.dict_mixers['dsp_load'], self.dict_mixers['mixers'])
		for i in range(len(objcmds)):
			objcmds[i].exe_command()

	def dsp_unload(self):
		objcmds = self.get_bulk_command(self.prefix, self.dict_mixers['dsp_unload'], self.dict_mixers['mixers'])
		for i in range(len(objcmds)):
			objcmds[i].exe_command()

	def dsp_mute(self):
		objcmd = self.get_command(self.prefix, self.dict_mixers['dsp_mute'][0], self.dict_mixers['mixers'])
		objcmd.exe_command()

	def dsp_unmute(self):
		objcmd = self.get_command(self.prefix, self.dict_mixers['dsp_unmute'][0], self.dict_mixers['mixers'])
		objcmd.exe_command()

	def dump_regs(self):
		dbgfs = debugfs.debugfs()
		dbgfs.regs_dump(self.bus)

	def reg_write(self, reg, val):
		dbgfs = debugfs.debugfs()
		dbgfs.reg_write(self.bus, reg, val)

	def reg_read(self, reg):
		dbgfs = debugfs.debugfs()
		dbgfs.reg_read(self.bus, reg)

	def get_type(self):
		return self.type

	def get_bus(self):
		return self.bus

	def get_addr(self):
		return self.addr

	def get_prefix(self):
		return self.prefix

	def get_mixers(self):
		return self.dict_mixers

	def get_rtlog_init(self):
		return self.dict_mixers['rtlog_init']

	def get_rtlog_get(self):
		return self.dict_mixers['rtlog_get']

	def get_mute(self):
		return self.dict_mixers['dsp_mute']

	def get_unmute(self):
		return self.dict_mixers['dsp_unmute']

	def get_temp(self):
		return self.dict_mixers['dsp_temp']

	def get_cali(self):
		return self.dict_mixers['dsp_cali']

	def get_load(self):
		return self.dict_mixers['dsp_load']

	def get_unload(self):
		return self.dict_mixers['dsp_unload']

	def get_firmware(self):
		return self.dict_mixers['spk_firmware']

	def amp_route(self, path):
		print sys._getframe().f_code.co_name
		return

	def amp_reg_dump():
		print sys._getframe().f_code.co_name

	def amp_reg_set(addr, value):
		print sys._getframe().f_code.co_name

	def amp_reg_get(addr):
		print sys._getframe().f_code.co_name
