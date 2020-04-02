#!/usr/bin/env python3
#  Given a list of items on stdin, display them on stderr and
#  then read keystrokes from the user to match the items.
#  Upon selection, print the entire line selected to stdout.
#
#  The first column is a key field: an exact match from user entry
#  will cause immediate completion without ENTER.

#  Because select-line doesn't output to stdout until completion, it
#  is easy to use from subshells in command substitution contexts.

import sys
import os
import curses

def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

getch = _find_getch()

def main(win):
    win.nodelay(True)
    key=""
    #win.clear()
    win.addstr("Detected key:")
    while 1:
        try:
           key = win.getkey()
           #win.clear()
           win.addstr("Detected key:")
           win.addstr(str(key))
           if key == os.linesep:
              break
        except Exception as e:
           # No input
           pass


if __name__ == "__main__":
    liststream=sys.stdin
    try:
        if os.path.isfile(sys.argv[1]):
            liststream = open( sys.argv[1], 'r')
    except:
        pass

    items = liststream.read().split('\n')
    sys.stderr.write( '\n'.join(items))
    curses.wrapper(main)

