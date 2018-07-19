#!/usr/bin/python3

import os
import sys
import commands
import time
import argparse
import m1882
import rtlog

import tparser
from decimal import Decimal
from rtlog import Rtlog

#start here

rt = Rtlog()

#adb init
rt.init(0)
parser = argparse.ArgumentParser()
rt.argument(parser)
arg = parser.parse_args()
rt.args_send(arg)



