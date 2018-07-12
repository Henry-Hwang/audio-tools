import os
import sys
import commands
import time
import argparse
import csdevs
import tparser
import tinycmd

from decimal import Decimal

class m1882():
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
	_spk_firmware = ["DSP1 Firmware,\"Protection Right\"",]
	_rcv_firmware = ["DSP1 Firmware,\"Protection Left\"",]

	def __init__(self):
		self.cs35l35_r = csdevs.cs35l41(1, "spi1.0", 0, "SPK",
							self._dsp_mixers,
							self._rtlog_init,
							self._rtlog_get,
							self._dsp_mute,
							self._dsp_unmute,
							self._dsp_temp,
							self._dsp_cali,
							self._dsp_load,
							self._dsp_unload,
							self._spk_firmware)
		self.cs35l35_l = csdevs.cs35l41(1, "spi1.1", 0, "RCV",
							self._dsp_mixers,
							self._rtlog_init,
							self._rtlog_get,
							self._dsp_mute,
							self._dsp_unmute,
							self._dsp_temp,
							self._dsp_cali,
							self._dsp_load,
							self._dsp_unload,
							self._rcv_firmware)

	def show_prot(self, spk):
		if(spk == "SPK"):
			self.cs35l35_r.show_prot()
		if(spk == "RCV"):
			self.cs35l35_l.show_prot()
		if(spk == "BOTH"):
			self.cs35l35_r.show_prot()

	def dsp_reload(self, spk):
		if(spk == "SPK"):
			self.cs35l35_r.dsp_unload()
			time.sleep(1)
			self.cs35l35_r.dsp_load()
		if(spk == "RCV"):
			self.cs35l35_l.dsp_unload()
			time.sleep(1)
			self.cs35l35_l.dsp_load()
		if(spk == "BOTH"):
			self.cs35l35_r.dsp_unload()
			time.sleep(1)
			self.cs35l35_r.dsp_load()

	def dsp_load(self, spk):
		if(spk == "SPK"):
			self.cs35l35_r.dsp_load()
		if(spk == "RCV"):
			self.cs35l35_l.dsp_load()
		if(spk == "BOTH"):
			self.cs35l35_r.dsp_load()

	def dsp_unload(self, spk):
		if(spk == "SPK"):
			self.cs35l35_r.dsp_unload()
		if(spk == "RCV"):
			self.cs35l35_l.dsp_unload()
		if(spk == "BOTH"):
			self.cs35l35_r.dsp_unload()

	def dsp_mute(self, spk):
		if(spk == "SPK"):
			self.cs35l35_r.dsp_mute()
		if(spk == "RCV"):
			self.cs35l35_l.dsp_mute()
		if(spk == "BOTH"):
			self.cs35l35_r.dsp_mute()

	def dsp_unmute(self, spk):
		if(spk == "SPK"):
			self.cs35l35_r.dsp_unmute()
		if(spk == "RCV"):
			self.cs35l35_l.dsp_unmute()
		if(spk == "BOTH"):
			self.cs35l35_r.dsp_unmute()

	def dump_regs(self, spk):
		if(spk == "SPK"):
			self.cs35l35_r.dump_regs()
		if(spk == "RCV"):
			self.cs35l35_l.dump_regs()

	def reg_write(self, args):
		if(args[0] == "SPK"):
			self.cs35l35_r.reg_write(args[1], args[2])
		if(args[0] == "RCV"):
			self.cs35l35_l.reg_write(args[1], args[2])

	def reg_read(self, args):
		if(args[0] == "SPK"):
			self.cs35l35_r.reg_read(args[1])
		if(args[0] == "RCV"):
			self.cs35l35_l.reg_read(args[1])

	def stereo_show_prot(self, z_min_r, z_max_r, temp_r):
		z_min_r =  z_min_r * Decimal(self.get_factor())
		z_max_r =  z_max_r * Decimal(self.get_factor())
		print "(%3.2f" % z_min_r, " %3.2f )ohm"  % z_max_r, "  T (%3.2f)" %temp_r



