#!/usr/bin/python3

import os
import sys
import commands
import time
import argparse
import m1882
import adb
import debugfs
import tparser
from decimal import Decimal
from m1882 import M1882
from m1872 import M1872

from adb import Adb
from debugfs import Debugfs

class Rtlog(M1882, Adb, Debugfs):
	def __init__(self):
		super(Rtlog,self).__init__()
		#M1882.__init__()
		#Adb.__init__()
	def argument(self, parser):
		M1882.argument(self, parser)
		Adb.argument(self, parser)
		Debugfs.argument(self, parser)
	def args_send(self, arg):
		M1882.args_send(self, arg)
		Adb.args_send(self, arg)
		Debugfs.args_send(self, arg)