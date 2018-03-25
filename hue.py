#!/usr/bin/env python

COMMANDS = {
    # Lables
    'info': (33, '[!] '),
    'que': (34, '[?] '),
    'bad': (31, '[-] '),
    'good': (32, '[+] '),
    'run': (97, '[~] '),

    # Colors
    'green': 32,
    'lightgreen': 92,
    'grey': 37,
    'black': 30,
    'red': 31,
    'lightred': 91,
    'cyan': 36,
    'lightcyan': 96,
    'blue': 34,
    'lightblue': 94,
    'purple': 35,
    'yellow': 93,
    'white': 97,
    'lightpurple': 95,
    'orange': 33,

    # Styles
    'bg': ';7',
    'bold': ';1',
    'italic': '3',
    'under': '4',
    'strike': '09',
}

enabled = True


def _gen(string, prefix, key):
    if not enabled:
        return string
    colored = prefix if prefix else string
    not_colored = string if prefix else ''
    return '\033[{}m{}\033[0m{}'.format(key, colored, not_colored)


def hue_enable_windows_support():
    """
    Enables ANSI Support on Windows 10, disables ansi characters otherwise
    :return Whether can enable windows support
    """
    import os
    if os.name != "nt":
        # Return true on anything other than windows
        return True
    try:
        # https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences#span-idsamplesspanspan-idsamplesspanspan-idsamplesspansamples
        # https://docs.microsoft.com/en-us/windows/console/getstdhandle
        # https://docs.microsoft.com/en-us/windows/console/getconsolemode
        # https://docs.microsoft.com/en-us/windows/console/setconsolemode

        # Also, logic from https://github.com/ogham/rust-ansi-term/blob/master/src/windows.rs, was the simplest to fit into python

        import ctypes
        import ctypes.wintypes

        kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        error_code = kernel32.GetLastError()
        if error_code != 0:
            return False
        kernel32.GetStdHandle.restype = ctypes.wintypes.HANDLE

        STD_OUTPUT_HANDLE = -11
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

        hout = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)  # STD_OUTPUT_HANDLE = -11
        error_code = kernel32.GetLastError()
        if error_code != 0:
            return False
        dwOriginalOutMode = ctypes.c_uint32(0)
        kernel32.GetConsoleMode(hout, ctypes.byref(dwOriginalOutMode))
        error_code = kernel32.GetLastError()
        if error_code != 0:
            return False
        dwOriginalOutMode = dwOriginalOutMode.value
        # if not enabled
        if dwOriginalOutMode & ENABLE_VIRTUAL_TERMINAL_PROCESSING == 0:
            kernel32.SetConsoleMode(hout, ctypes.c_uint32(dwOriginalOutMode | ENABLE_VIRTUAL_TERMINAL_PROCESSING))
            error_code = kernel32.GetLastError()
            if error_code != 0:
                return False

        return True
    except ImportError:
        return False


def hue_enable():
    global enabled
    enabled = True


def hue_disable():
    global enabled
    enabled = False


for key, val in COMMANDS.items():
    value = val[0] if isinstance(val, tuple) else val
    prefix = val[1] if isinstance(val, tuple) else ''
    locals()[key] = lambda s, prefix=prefix, key=value: _gen(s, prefix, key)

__all__ = list(COMMANDS.keys()) + ['hue_enable_windows_support', 'hue_enable', 'hue_disable']
