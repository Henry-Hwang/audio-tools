#!/usr/bin/python3

import os
import sys
import commands
import time
import argparse
import m1882
import adb
import tparser
from decimal import Decimal
from m1882 import M1882
from m1872 import M1872

from adb import Adb
class Rtlog(M1882, Adb):
	def __init__(self):
		super(Rtlog,self).__init__()
		#M1882.__init__()
		#Adb.__init__()
	def argument(self, parser):
		M1882.argument(self, parser)
		Adb.argument(self, parser)
	def args_send(self, arg):
		M1882.args_send(self, arg)
		Adb.args_send(self, arg)