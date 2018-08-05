import os
import sys
import commands
import time
import argparse
import tparser
import tinycmd

from decimal import Decimal
from widget import Widget
class Dpath(object):
	widgets = []

	def __init__(self):
		# without init will cause memery over write
		self.widgets = []

	def add_widget(self, widget):
		self.widgets.append(widget)

	def add_widgets(self, widgets):
		self.widgets.extend(widgets)
