from hue import COMMANDS

__all__ = list(COMMANDS.keys())
__version__ = '1.0.1'

if __name__ == '__main__':
    print('All commands: ', __all__)
    print('Current version: ', __version__)
