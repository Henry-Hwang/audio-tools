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

class Cs35l41(amplifier.Amplifier):
	name = "CS35L41"
	factor = 5.857143

	def __init__(self, type, bus, addr, prefix, firmware, dict_mixers):
		super(Cs35l41,self).__init__(type, bus, addr, prefix, firmware, self.factor, self.name, dict_mixers)






