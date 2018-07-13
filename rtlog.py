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
from adb import Adb
class Rtlog(M1882, Adb):
	def __init__(self):
			super(Rtlog,self).__init__()
