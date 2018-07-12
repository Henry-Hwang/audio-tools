import os
import sys
import commands
import time
import argparse
import cscore
import tinycmd
import tparser
import debugfs
from decimal import Decimal

class cs35l41(cscore.amplifier):
	name = "CS35L41"
	factor = 5.857143

	def __init__(self, type, bus, addr, prefix, mixers, rtlog_init, rtlog_get, mute, unmute, temp, cali, load, unload, firmware):
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
		super(cs35l41,self).__init__( type, bus, addr, prefix, mixers, rtlog_init, rtlog_get, mute, unmute, temp, cali, load, unload, firmware)

	def get_factor(self):
		return self.factor


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

	def get_prot(self, result, temp_h):
		parser = tparser.parser()
		temp = parser.n1_32bit_str(temp_h)
		z_min, z_max, factor_min, factor_max = parser.n4_32bit_str(result)
		temp = parser.to_decimal(temp, 10, 13)
		z_min = parser.to_decimal(z_min, 10, 13)
		z_max = parser.to_decimal(z_max, 10, 13)
		factor_min = parser.to_decimal(factor_min, 5, 18)
		factor_max = parser.to_decimal(factor_max, 5, 18)

		return z_min, z_max, temp, factor_max

	def dsp_load(self):
		objcmd = self.get_command(self.prefix, self.mixer_firmware[0], self.mixers)
		objcmd.exe_command()

		objcmds = self.get_bulk_command(self.prefix, self.mixer_load, self.mixers)
		for i in range(len(objcmds)):
			objcmds[i].exe_command()

	def dsp_unload(self):
		objcmds = self.get_bulk_command(self.prefix, self.mixer_unload, self.mixers)
		for i in range(len(objcmds)):
			objcmds[i].exe_command()

	def dsp_mute(self):
		objcmd = self.get_command(self.prefix, self.mixer_mute[0], self.mixers)
		objcmd.exe_command()

	def dsp_unmute(self):
		objcmd = self.get_command(self.prefix, self.mixer_unmute[0], self.mixers)
		objcmd.exe_command()

	def dump_regs(self):
		dbgfs = debugfs.debugfs()
		dbgfs.dump_registers(self.bus)

	def reg_write(self, reg, val):
		dbgfs = debugfs.debugfs()
		dbgfs.reg_write(self.bus, reg, val)

	def reg_read(self, reg):
		dbgfs = debugfs.debugfs()
		dbgfs.reg_read(self.bus, reg)

	def show_prot(self):
		objcmds = self.get_bulk_command(self.prefix, self.mixer_rtlog_init, self.mixers)
		for i in range(len(objcmds)):
			objcmds[i].exe_command()

		print "----------------------------------------"
		for i in range(100):
			objcmd = self.get_command(self.prefix, self.mixer_temp[0], self.mixers)
			temp = objcmd.exe_get_command()

			objcmd = self.get_command(self.prefix, self.mixer_rtlog_get[0], self.mixers)
			result = objcmd.exe_get_command()
			z_min, z_max, temp, factor_max = self.get_prot(result, temp)
			z_min =  z_min * Decimal(self.factor)
			z_max =  z_max * Decimal(self.factor)

			print "(%3.2f" % z_min, " %3.2f )ohm"  % z_max, "  T (%3.2f)" %temp

