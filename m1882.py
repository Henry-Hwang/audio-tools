import os
import sys
import commands
import time
import argparse
import cs35l41
import tparser
import tinycmd
from cs35l41 import Cs35l41
from asoc import Asoc
from decimal import Decimal

class M1882(object):
	name = "1882"

	_dsp_mixers = ["RCV DSP1X Protection L 4a4 config_XM_stru",
					"RCV DSP1X Protection L 4a4 HALO_STATE",
					"RCV DSP1X Protection L 4a4 HALO_HEARTBEAT",
					"RCV DSP1X Protection L 4a4 AUDIO_BLK_SIZE",
					"RCV DSP1X Protection L 4a4 BUILD_JOB_NAME",
					"RCV DSP1X Protection L 4a4 BUILD_JOB_NUMB",
					"RCV DSP1X Protection L cd cspl_XM_struct_t",
					"RCV DSP1X Protection L cd CSPL_ENABLE",
					"RCV DSP1X Protection L cd CSPL_COMMAND",
					"RCV DSP1X Protection L cd CSPL_STATE",
					"RCV DSP1X Protection L cd CSPL_ERRORNO",
					"RCV DSP1X Protection L cd CSPL_TEMPERATURE",
					"RCV DSP1X Protection L cd UPDT_PRMS",
					"RCV DSP1X Protection L cd CAL_R",
					"RCV DSP1X Protection L cd CAL_AMBIENT",
					"RCV DSP1X Protection L cd CAL_STATUS",
					"RCV DSP1X Protection L cd CAL_CHECKSUM",
					"RCV DSP1X Protection L cd CAL_SET_STATUS",
					"RCV DSP1X Protection L cd DIAG_F0",
					"RCV DSP1X Protection L cd DIAG_Z_LOW_DIFF",
					"RCV DSP1X Protection L cd DIAG_F0_STATUS",
					"RCV DSP1X Protection L cd RTLOG_ENABLE",
					"RCV DSP1X Protection L cd RTLOG_CAN_READ",
					"RCV DSP1X Protection L cd RTLOG_COUNT",
					"RCV DSP1X Protection L cd RTLOG_TIMER",
					"RCV DSP1X Protection L cd RTLOG_FRAMECOUNTE",
					"RCV DSP1X Protection L cd RAMESPERCAPTUREWI",
					"RCV DSP1X Protection L cd RTLOG_VARIABLE",
					"RCV DSP1X Protection L cd RTLOG_DATA",
					"RCV DSP1X Protection L cd BDLOG_MAX_TEMP",
					"RCV DSP1X Protection L cd BDLOG_MAX_EXC",
					"RCV DSP1X Protection L cd BDLOG_OVER_TEMP_C",
					"RCV DSP1X Protection L cd BDLOG_OVER_EXC_CO",
					"RCV DSP1X Protection L cd BDLOG_ABNORMAL_MU",
					"RCV DSP1X Protection L cd REDUCE_POWER",
					"RCV DSP1X Protection L cd DEBUGMDRXERR",
					"RCV DSP1X Protection L cd MDSYNCNOUPDATECNT",
					"SPK DSP1X Protection R 4a4 config_XM_stru",
					"SPK DSP1X Protection R 4a4 HALO_STATE",
					"SPK DSP1X Protection R 4a4 HALO_HEARTBEAT",
					"SPK DSP1X Protection R 4a4 AUDIO_BLK_SIZE",
					"SPK DSP1X Protection R 4a4 BUILD_JOB_NAME",
					"SPK DSP1X Protection R 4a4 BUILD_JOB_NUMB",
					"SPK DSP1X Protection R cd cspl_XM_struct_t",
					"SPK DSP1X Protection R cd CSPL_ENABLE",
					"SPK DSP1X Protection R cd CSPL_COMMAND",
					"SPK DSP1X Protection R cd CSPL_STATE",
					"SPK DSP1X Protection R cd CSPL_ERRORNO",
					"SPK DSP1X Protection R cd CSPL_TEMPERATURE",
					"SPK DSP1X Protection R cd UPDT_PRMS",
					"SPK DSP1X Protection R cd CAL_R",
					"SPK DSP1X Protection R cd CAL_AMBIENT",
					"SPK DSP1X Protection R cd CAL_STATUS",
					"SPK DSP1X Protection R cd CAL_CHECKSUM",
					"SPK DSP1X Protection R cd CAL_SET_STATUS",
					"SPK DSP1X Protection R cd DIAG_F0",
					"SPK DSP1X Protection R cd DIAG_Z_LOW_DIFF",
					"SPK DSP1X Protection R cd DIAG_F0_STATUS",
					"SPK DSP1X Protection R cd RTLOG_ENABLE",
					"SPK DSP1X Protection R cd RTLOG_CAN_READ",
					"SPK DSP1X Protection R cd RTLOG_COUNT",
					"SPK DSP1X Protection R cd RTLOG_TIMER",
					"SPK DSP1X Protection R cd RTLOG_FRAMECOUNTE",
					"SPK DSP1X Protection R cd RAMESPERCAPTUREWI",
					"SPK DSP1X Protection R cd RTLOG_VARIABLE",
					"SPK DSP1X Protection R cd RTLOG_DATA",
					"SPK DSP1X Protection R cd BDLOG_MAX_TEMP",
					"SPK DSP1X Protection R cd BDLOG_MAX_EXC",
					"SPK DSP1X Protection R cd BDLOG_OVER_TEMP_C",
					"SPK DSP1X Protection R cd BDLOG_OVER_EXC_CO",
					"SPK DSP1X Protection R cd BDLOG_ABNORMAL_MU",
					"SPK DSP1X Protection R cd REDUCE_POWER",
					"SPK DSP1X Protection R cd DEBUGMDRXERR",
					"SPK DSP1X Protection R cd MDSYNCNOUPDATECNT",
					"SPK PCM Source",
					"SPK DSP1 Firmware",
					"SPK AMP Enable Switch",
					"SPK DSP Booted",
					"RCV PCM Source",
					"RCV DSP1 Firmware",
					"RCV AMP Enable Switch",
					"RCV DSP Booted",
					]


	_rtlog_init = ["RAMESPERCAPTUREWI,		0x00 0x00 0x07 0xD0",
					"RTLOG_VARIABLE,		0x00 0x00 0x03 0x9D 0x00 0x00 0x03 0xAE",
					"RTLOG_COUNT,			0x00 0x00 0x00 0x02",
					"RTLOG_CAN_READ,		0x00 0x00 0x00 0x02",
					"RTLOG_ENABLE,			0x00 0x00 0x00 0x01",]
	_rtlog_get = ["RTLOG_DATA,",]
	_dsp_mute = ["CSPL_COMMAND,	0x00 0x00 0x00 0x01", "dsfsd"]
	_dsp_unmute = ["CSPL_COMMAND,	0x00 0x00 0x00 0x02",]
	_dsp_temp = ["CSPL_TEMPERATURE,",]
	_dsp_cali = ["CAL_R,",]

	_dsp_load = ["PCM Source,			DSP",
				   "AMP Enable Switch,	1",]
	_dsp_unload = ["DSP Booted,		0",
					"AMP Enable Switch,	0",]
	_spk_firmware = ["DSP1 Firmware,\'Protection Right\'",]
	_rcv_firmware = ["DSP1 Firmware,\'Protection Left\'",]

	dict_mixers={"mixers":_dsp_mixers, "rtlog_init":_rtlog_init,
				"rtlog_get":_rtlog_get, "dsp_mute":_dsp_mute,
				"dsp_unmute":_dsp_unmute, "dsp_temp":_dsp_temp,
				"dsp_cali":_dsp_cali, "dsp_load":_dsp_load,
				"dsp_unload":_dsp_unload, "spk_firmware":_spk_firmware,
				"rcv_firmware":_rcv_firmware};

	codec_filter = ["spi1.0", "spi1.1"]

	def __init__(self):
		self.cs35l41_r = Cs35l41(1, "spi1.0", 0, "SPK",
							self._spk_firmware, self.dict_mixers)
		self.cs35l41_l = Cs35l41(1, "spi1.1", 0, "RCV",
							self._rcv_firmware, self.dict_mixers)

	def show_prot(self, spk):
		if(spk == "SPK"):
			self.cs35l41_r.show_prot()
		if(spk == "RCV"):
			self.cs35l41_l.show_prot()
		if(spk == "BOTH"):
			self.cs35l41_r.show_prot()

	def reload(self, spk):
		if(spk == "SPK"):
			self.cs35l41_r.dsp_unload()
			time.sleep(1)
			self.cs35l41_r.dsp_load()
		if(spk == "RCV"):
			self.cs35l41_l.dsp_unload()
			time.sleep(1)
			self.cs35l41_l.dsp_load()
		if(spk == "BOTH"):
			self.cs35l41_r.dsp_unload()
			time.sleep(1)
			self.cs35l41_r.dsp_load()

	def load(self, spk):
		if(spk == "SPK"):
			self.cs35l41_r.dsp_load()
		if(spk == "RCV"):
			self.cs35l41_l.dsp_load()
		if(spk == "BOTH"):
			self.cs35l41_r.dsp_load()

	def unload(self, spk):
		if(spk == "SPK"):
			self.cs35l41_r.dsp_unload()
		if(spk == "RCV"):
			self.cs35l41_l.dsp_unload()
		if(spk == "BOTH"):
			self.cs35l41_r.dsp_unload()

	def mute(self, spk):
		if(spk == "SPK"):
			self.cs35l41_r.dsp_mute()
		if(spk == "RCV"):
			self.cs35l41_l.dsp_mute()
		if(spk == "BOTH"):
			self.cs35l41_r.dsp_mute()

	def unmute(self, spk):
		if(spk == "SPK"):
			self.cs35l41_r.dsp_unmute()
		if(spk == "RCV"):
			self.cs35l41_l.dsp_unmute()
		if(spk == "BOTH"):
			self.cs35l41_r.dsp_unmute()

	def dump_regs(self, spk):
		if(spk == "SPK"):
			self.cs35l41_r.dump_regs()
		if(spk == "RCV"):
			self.cs35l41_l.dump_regs()

	def reg_write(self, args):
		if(args[0] == "SPK"):
			self.cs35l41_r.reg_write(args[1], args[2])
		if(args[0] == "RCV"):
			self.cs35l41_l.reg_write(args[1], args[2])

	def reg_read(self, args):
		if(args[0] == "SPK"):
			self.cs35l41_r.reg_read(args[1])
		if(args[0] == "RCV"):
			self.cs35l41_l.reg_read(args[1])

	def debug(self, args):
		'''
		#cmdstr = "adb shell  find /proc/asound/card0/ -name status"
		cmdstr = "adb shell  find /d/asoc/ -name \* "
		print cmdstr
		result = os.popen(cmdstr)
		ret = result.read()
		paths = ret.split('\n')
		#asoc_t = Asoc()
		for i in range(len(paths)):
			print paths[i]
			#result = os.popen("adb shell cat " + paths[i])
			#ret = result.read()
			#if (ret.strip() != "closed"):
			#	print ret
		'''
		asoc = Asoc(self.codec_filter)
		asoc.find_codecs()
		asoc.get_snd_cards()
		asoc.find_snd_cards()
		c = asoc.get_on_widgets("sdm845-tavil-snd-card", "spi1.0")
		#c = asoc.get_widgets("sdm845-tavil-snd-card", "spi1.1")
		#c = asoc.get_codecs("sdm845-tavil-snd-card")

		for i in range(len(c)):
			print c[i].name


		#print ret

	def argument(self):
		parser = argparse.ArgumentParser()
		parser.add_argument("-ai", "--adb", required=False, help="adb init", type=str)
		parser.add_argument("-ap", "--adb-push", required=False, help="adb push", nargs=2, type=str)
		parser.add_argument("-wi", "--wisce-init", required=False, help="adb push", type=str)
		parser.add_argument("-de", "--debug", required=False, help="debug", type=str)

		parser.add_argument('-s', "--show-prot", required=False, help="display infomation of a given number", type=str)
		parser.add_argument("-rl", "--reload", required=False, help="reload firmware for SPK/RCV", type=str)
		parser.add_argument("-ld", "--load", required=False, help="reload firmware for SPK/RCV", type=str)
		parser.add_argument("-ul", "--unload", required=False, help="reload firmware for SPK/RCV", type=str)
		parser.add_argument("-mt", "--mute", required=False, help="mute AMP, SPK/RCV", type=str)
		parser.add_argument("-um", "--unmute", required=False, help="unmute AMP, SPK/RCV", type=str)
		parser.add_argument("-dr", "--dump-regs", required=False, help="dump registers", type=str)
		parser.add_argument("-dl", "--dmesg-loop", required=False, help="dmesg loop message", type=str)
		parser.add_argument("-w", "--write", required=False, help="write [SPK, reg, val]", nargs=3, type=str)
		parser.add_argument("-r", "--read", required=False, help="read [SPK, reg]", nargs=2, type=str)

		return parser

	def args_send(self, arg):
		if arg.debug:
			self.debug(arg.debug)
		if arg.dmesg_loop:
			self.dmesg_loop(arg.dmesg_loop)
		if arg.adb:
			self.adb(arg.adb)
		if arg.adb_push:
			self.adb_push(arg.adb_push)
		if arg.wisce_init:
			self.wisce_init(arg.wisce_init)
		if arg.dump_regs:
			self.dump_regs(arg.dump_regs)
		if arg.show_prot:
			self.show_prot(arg.show_prot)
		if arg.reload:
			self.reload(arg.reload)
		if arg.load:
			self.load(arg.load)
		if arg.unload:
			self.unload(arg.unload)
		if arg.mute:
			self.mute(arg.mute)
		if arg.unmute:
			self.unmute(arg.unmute)
		if arg.write:
			self.reg_write(arg.write)
		if arg.read:
			self.reg_read(arg.read)


