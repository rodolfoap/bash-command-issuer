#!/usr/bin/python3
import sys
from pynput import keyboard # Requires: pip install pynput

# An [ENTER] keypress signal can be sent after writing each line
# By default, better to disable it, so commands can be edited.
SEND_ENTER=False

class Issuer:
	def __init__(this):
		with open('commands.list') as file: this.lines=[line.rstrip() for line in file]
		print("LINES READ:", this.lines)
		this.line=0
		this.sender=keyboard.Controller()
		with keyboard.Listener(on_press=this.on_press) as listener: listener.join()
	def on_press(this, key):
		try:
			print('{0}'.format(key.char), end='')
			sys.stdout.flush()
		except AttributeError:
			if key==keyboard.Key.pause:
				print('>>> ', end='')
				for key in this.lines[this.line]:
					this.sender.press(key)
					this.sender.release(key)
				print()
				this.line+=1
				if this.line==len(this.lines):
					print('EOF reached.\n')
					return False

				if SEND_ENTER:
					this.sender.press(keyboard.Key.enter)
					this.sender.release(keyboard.Key.enter)
			else:
				print('[{0}]'.format(key))

Issuer()
