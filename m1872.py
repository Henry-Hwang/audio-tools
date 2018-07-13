import os
import sys
import commands
import time
import argparse
import cs35l41
import tparser
import tinycmd

from decimal import Decimal

class M1872():
	name ="1872"

	_dsp_mixers = [
					"SPK DSP1X Protection 400a4 m_config_XM_stru",
					"SPK DSP1X Protection 400a4 HALO_STATE",
					"SPK DSP1X Protection 400a4 HALO_HEARTBEAT",
					"SPK DSP1X Protection cd _FRAMESPERCAPTUREWI",
					"SPK DSP1X Protection cd RTLOG_VARIABLE",
					"SPK DSP1X Protection 400a4 BUILD_JOB_NAME",
					"SPK DSP1X Protection 400a4 AUDIO_BLK_SIZE",
					"SPK DSP1X Protection cd BDLOG_MAX_EXC",
					"SPK DSP1X Protection 400a4 BUILD_JOB_NUMBER",
					"SPK DSP1X Protection cd BDLOG_OVER_TEMP_COU",
					"SPK DSP1X Protection cd cspl_XM_struct_t",
					"SPK DSP1X Protection cd BDLOG_OVER_EXC_COUN",
					"SPK DSP1X Protection cd CSPL_ENABLE",
					"SPK DSP1X Protection cd BDLOG_ABNORMAL_MUTE",
					"SPK DSP1X Protection cd CSPL_COMMAND",
					"SPK DSP1X Protection cd RTLOG_DATA",
					"SPK DSP1X Protection cd CSPL_STATE",
					"SPK DSP1X Protection cd BDLOG_MAX_TEMP",
					"SPK DSP1X Protection cd REDUCE_POWER",
					"SPK DSP1X Protection cd DEBUGMDRXERR",
					"SPK DSP1X Protection cd MDSYNCNOUPDATECNT",
					"SPK DSP1X Protection cd CSPL_TEMPERATURE",
					"SPK DSP1X Protection cd CAL_AMBIENT",
					"SPK DSP1X Protection cd CSPL_ERRORNO",
					"SPK DSP1X Protection cd UPDT_PRMS",
					"SPK DSP1X Protection cd CAL_R",
					"SPK DSP1X Protection cd CAL_STATUS",
					"SPK DSP1X Protection cd CAL_CHECKSUM",
					"SPK DSP1X Protection cd CAL_SET_STATUS",
					"SPK DSP1X Protection cd DIAG_F0",
					"SPK DSP1X Protection cd DIAG_Z_LOW_DIFF",
					"SPK DSP1X Protection cd DIAG_F0_STATUS",
					"SPK DSP1X Protection cd RTLOG_ENABLE",
					"SPK DSP1X Protection cd RTLOG_CAN_READ",
					"SPK DSP1X Protection cd RTLOG_COUNT",
					"SPK DSP1X Protection cd RTLOG_TIMER",
					"SPK DSP1X Protection cd RTLOG_FRAMECOUNTER",
					"SPK PCM Source",
					"SPK DSP1 Firmware",
					"SPK AMP Enable Switch",
					"SPK DSP Booted",
					]


	_rtlog_init = ["RAMESPERCAPTUREWI,		0x00 0x00 0x07 0xD0",
					"RTLOG_VARIABLE,		0x00 0x00 0x03 0x9D 0x00 0x00 0x03 0xAE",
					"RTLOG_COUNT,			0x00 0x00 0x00 0x02",
					"RTLOG_CAN_READ,		0x00 0x00 0x00 0x02",
					"RTLOG_ENABLE,			0x00 0x00 0x00 0x01",]
	_rtlog_get = ["RTLOG_DATA,",]
	_dsp_mute = ["CSPL_COMMAND,	0x00 0x00 0x00 0x01",]
	_dsp_unmute = ["CSPL_COMMAND,	0x00 0x00 0x00 0x02",]
	_dsp_temp = ["CSPL_TEMPERATURE,",]
	_dsp_cali = ["CAL_R,",]

	_dsp_load = ["PCM Source,			DSP",
				"AMP Enable Switch,	1",]
	_dsp_unload = ["DSP Booted,		0",
					"AMP Enable Switch,	0",]
	_spk_firmware = ["DSP1 Firmware,Protection",]
	_rcv_firmware = ["DSP1 Firmware,Protection",]

	def __init__(self):
		self.cs35l41_r = cs35l41.cs35l41(1,"spi1.0", 0,"SPK",
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
		self.cs35l41_l = cs35l41.cs35l41(1,"spi1.1", 0,"RCV",
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
		if(spk =="SPK"):
			self.cs35l41_r.show_prot()
		if(spk =="RCV"):
			self.cs35l41_l.show_prot()
		if(spk =="BOTH"):
			self.cs35l41_r.show_prot()

	def dsp_reload(self, spk):
		if(spk =="SPK"):
			self.cs35l41_r.dsp_unload()
			time.sleep(1)
			self.cs35l41_r.dsp_load()
		if(spk =="RCV"):
			self.cs35l41_l.dsp_unload()
			time.sleep(1)
			self.cs35l41_l.dsp_load()
		if(spk =="BOTH"):
			self.cs35l41_r.dsp_unload()
			time.sleep(1)
			self.cs35l41_r.dsp_load()

	def dsp_load(self, spk):
		if(spk =="SPK"):
			self.cs35l41_r.dsp_load()
		if(spk =="RCV"):
			self.cs35l41_l.dsp_load()
		if(spk =="BOTH"):
			self.cs35l41_r.dsp_load()

	def dsp_unload(self, spk):
		if(spk =="SPK"):
			self.cs35l41_r.dsp_unload()
		if(spk =="RCV"):
			self.cs35l41_l.dsp_unload()
		if(spk =="BOTH"):
			self.cs35l41_r.dsp_unload()

	def dsp_mute(self, spk):
		if(spk =="SPK"):
			self.cs35l41_r.dsp_mute()
		if(spk =="RCV"):
			self.cs35l41_l.dsp_mute()
		if(spk =="BOTH"):
			self.cs35l41_r.dsp_mute()

	def dsp_unmute(self, spk):
		if(spk =="SPK"):
			self.cs35l41_r.dsp_unmute()
		if(spk =="RCV"):
			self.cs35l41_l.dsp_unmute()
		if(spk =="BOTH"):
			self.cs35l41_r.dsp_unmute()

	def dump_regs(self, spk):
		if(spk =="SPK"):
			self.cs35l41_r.dump_regs()
		if(spk =="RCV"):
			self.cs35l41_l.dump_regs()

	def reg_write(self, args):
		if(args[0] =="SPK"):
			self.cs35l41_r.reg_write(args[1], args[2])
		if(args[0] =="RCV"):
			self.cs35l41_l.reg_write(args[1], args[2])

	def reg_read(self, args):
		if(args[0] =="SPK"):
			self.cs35l41_r.reg_read(args[1])
		if(args[0] =="RCV"):
			self.cs35l41_l.reg_read(args[1])



