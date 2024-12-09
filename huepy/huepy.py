#!/usr/bin/env python3

import ctypes
import platform

if platform.system() == 'Windows':
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

print_mode = False

COMMANDS = {
    # Labels
    'warn': (33, '[!] '),
    'info': (96, '[*] '),
    'que': (34, '[?] '),
    'bad': (31, '[-] '),
    'good': (32, '[+] '),
    'run': (97, '[~] '),

    # Colors
    'green': 32,
    'lgreen': 92,
    'lightgreen': 92,
    'grey': 37,
    'black': 30,
    'red': 31,
    'lred': 91,
    'lightred': 91,
    'cyan': 36,
    'lcyan': 96,
    'lightcyan': 96,
    'blue': 34,
    'lblue': 94,
    'lightblue': 94,
    'purple': 35,
    'yellow': 93,
    'white': 97,
    'lpurple': 95,
    'lightpurple': 95,
    'orange': 33,

    # Styles
    'bg': ';7',
    'bold': ';1',
    'italic': '3',
    'under': '4',
    'strike': '09',
}


def _gen(string, prefix, key):
    colored = prefix if prefix else string
    not_colored = string if prefix else ''
    result = '\033[{}m{}\033[0m{}'.format(key, colored, not_colored)
    if print_mode:
        print(result)
    else:
        return result


for key, val in COMMANDS.items():
    value = val[0] if isinstance(val, tuple) else val
    prefix = val[1] if isinstance(val, tuple) else ''
    locals()[key] = lambda s, prefix=prefix, key=value: _gen(s, prefix, key)
