#!/usr/bin/env python

# Labels

def info(string):
	return '\033[1;33m[!]\033[1;m ' + string

def que(string):
	return '\033[1;34m[?]\033[1;m ' + string

def bad(string):
	return '\033[1;31m[-]\033[1;m ' + string

def good(string):
	return '\033[1;32m[+]\033[1;m ' + string

def run(string):
	return '\033[1;97m[~]\033[1;m ' + string

# Colors

def green(string):
	return '\033[32m' + string + '\033[0m'

def lightgreen(string):
	return '\033[92m' + string + '\033[0m'

def grey(string):
	return '\033[37m' + string + '\033[0m'

def black(string):
	return '\033[30m' + string + '\033[0m'

def red(string):
	return '\033[31m' + string + '\033[0m'

def lightred(string):
	return '\033[91m' + string + '\033[0m'

def cyan(string):
	return '\033[36m' + string + '\033[0m'

def lightcyan(string):
	return '\033[96m' + string + '\033[0m'

def blue(string):
	return '\033[34m' + string + '\033[0m'

def lightblue(string):
	return '\033[94m' + string + '\033[0m'

def purple(string):
	return '\033[35m' + string + '\033[0m'

def yellow(string):
	return '\033[93m' + string + '\033[0m'

def white(string):
	return '\033[97m' + string + '\033[0m'

def lightpurple(string):
	return '\033[95m' + string + '\033[0m'

def orange(string):
	return '\033[33m' + string + '\033[0m'

# Styles

def bg(string):
	return '\033[;7m' + string + '\033[0m'

def bold(string):
	return '\033[;1m' + string + '\033[0m'

def italic(string):
	return '\033[3m' + string + '\033[0m'

def under(string):
	return '\033[4m' + string + '\033[0m'

def strike(string):
	return '\033[09m' + string + '\033[0m'
