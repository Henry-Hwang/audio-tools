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


'''
#start here

rtlog_adb(0)

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



#parser.print_help()
arg = parser.parse_args()
if arg.debug:
	rtlog_debug(arg.debug)
if arg.dmesg_loop:
	rtlog_dmesg_loop(arg.dmesg_loop)
if arg.adb:
	rtlog_adb(arg.adb)
if arg.adb_push:
	rtlog_adb_push(arg.adb_push)
if arg.wisce_init:
	rtlog_wisce_init(arg.wisce_init)
if arg.dump_regs:
	rtlog_dump_regs(arg.dump_regs)

if arg.show_prot:
	rtlog_show_prot(arg.show_prot)
if arg.reload:
	rtlog_reload(arg.reload)
if arg.load:
	rtlog_load(arg.load)
if arg.unload:
	rtlog_unload(arg.unload)
if arg.mute:
	rtlog_mute(arg.mute)
if arg.unmute:
	rtlog_unmute(arg.unmute)
if arg.write:
	rtlog_write(arg.write)
if arg.read:
	rtlog_read(arg.read)
else:
	print "adb init"

'''