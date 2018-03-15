#!/usr/bin/env python
from colorama import Style, Fore, init
from platform import system as getos
# Lables
init()

def info(string):
	return Fore.LIGHTYELLOW_EX + Style.BRIGHT + "[!] " + Style.RESET_ALL + string

def que(string):
	return Fore.LIGHTBLUE_EX + Style.BRIGHT + "[?] " + Style.RESET_ALL + string

def bad(string):
	return Fore.LIGHTRED_EX + Style.BRIGHT + "[-] " + Style.RESET_ALL + string

def good(string):
	return Fore.LIGHTGREEN_EX + Style.BRIGHT + "[+] " + Style.RESET_ALL + string

def run(string):
	return Fore.LIGHTWHITE_EX + Style.BRIGHT + "[~] " + Style.RESET_ALL + string

# Colors

def green(string):
	return Fore.GREEN + string + Style.RESET_ALL

def lightgreen(string):
	return Fore.LIGHTGREEN_EX + string + Style.RESET_ALL

def grey(string):
	return Fore.WHITE + string + Style.RESET_ALL

def black(string):
	return Fore.BLACK + string + Style.RESET_ALL

def red(string):
	return Fore.RED + string + Style.RESET_ALL

def lightred(string):
	return Fore.LIGHTRED_EX + string + Style.RESET_ALL

def cyan(string):
	return Fore.CYAN + string + Style.RESET_ALL

def lightcyan(string):
	return Fore.LIGHTCYAN_EX + string + Style.RESET_ALL

def blue(string):
	return Fore.BLUE + string + Style.RESET_ALL

def lightblue(string):
	return Fore.LIGHTBLUE_EX + string + Style.RESET_ALL

def purple(string):
	return Fore.MAGENTA + string + Style.RESET_ALL

def yellow(string):
	return Fore.LIGHTYELLOW_EX + string + Style.RESET_ALL

def white(string):
	return Fore.WHITE + string + Style.RESET_ALL

def lightpurple(string):
	return Fore.LIGHTMAGENTA_EX + string + Style.RESET_ALL

def orange(string):
	return Fore.YELLOW + string + Style.RESET_ALL

# Styles
if getos().lower()[0] != "w":
	def bg(string):
		return '\033[;7m' + string + Style.RESET_ALL

	def bold(string):
		return Style.BRIGHT + string + Style.RESET_ALL

	def italic(string):
		return '\033[3m' + string + '\033[0m'

	def under(string):
		return '\033[4m' + string + Style.RESET_ALL

	def strike(string):
		return '\033[09m' + string + Style.RESET_ALL
