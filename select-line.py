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

CTRL_C=3
ESC=27

def test_screenstuff():
    sys.stderr.write("\u001b[31mhello\u001b30m world")



def main(win):
    with open('slinput.log','w') as keylog:
        keylog.write("--Log opened--\n")

        test_screenstuff()

        #keylog.flush()
        sys.stderr.write( '\n'.join(items))
        getch = _find_getch()

        while True:
            try:
                key = getch()
                #import pudb
                #pudb.set_trace()
                keylog.write( f"Key rx: [{key}]:{len(key),ord(key)}\n")
                #keylog.flush()
                if key == 'x' or ord(key) == CTRL_C or ord(key) == ESC:
                    keylog.write("--quit--\n")
                    #keylog.flush()
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

    main(items)

