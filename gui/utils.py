"""Utils for logging, some helper functions, etc..."""
# coding=utf-8

RESET = '\u001b[0m'
CODES = {'black': '\u001b[30m', 'red': '\u001b[31m', 'green': '\u001b[32m',
         'yellow': '\u001b[33m', 'blue': '\u001b[34m', 'magenta': '\u001b[35m',
         'cyan': '\u001b[36m', 'white': '\u001b[37m',
         'backgroundBlack': '\u001b[40m', 'backgroundRed': '\u001b[41m',
         'backgroundGreen': '\u001b[42m', 'backgroundYellow': '\u001b[43m',
         'backgroundBlue': '\u001b[44m', 'backgroundMagenta': '\u001b[45m',
         'backgroundCyan': '\u001b[46m', 'backgroundWhite': '\u001b[47m',
         'bold': '\u001b[1m', 'underline': '\u001b[4m', 'reversed': '\u001b[7m'}


def dye(color, s):
    return CODES[color] + s + RESET
