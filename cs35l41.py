import os
import sys
import commands
import time
import argparse
import amplifier
import tinycmd
import tparser
import debugfs
from decimal import Decimal

class cs35l41(amplifier.amplifier):
	name = "CS35L41"
	factor = 5.857143

	def __init__(self, type, bus, addr, prefix, mixers, rtlog_init, rtlog_get, mute, unmute, temp, cali, load, unload, firmware):
		super(cs35l41,self).__init__( type, bus, addr, prefix, mixers, rtlog_init, rtlog_get, mute, unmute, temp, cali, load, unload, firmware, self.factor, self.name)





