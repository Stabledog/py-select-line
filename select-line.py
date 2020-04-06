#!/usr/bin/env python3
#  Given a list of items on stdin, display them on stderr and
#  then read keystrokes from the user to match the items.
#  Upon selection, print the entire line selected to stdout.
#
#  The first column is a key field: an exact match from user entry
#  will cause immediate completion without ENTER.

#  Because select-line doesn't output to stdout until completion, it
#  is easy to use from subshells in command substitution contexts.

import blessed  # See https://blessed.readthedocs.io/en/latest/api/terminal.html

import sys
import os


class FrameBuf(object):
    ''' Represents a framebuffer-like model of the text being presented: this is the
    raw content of the screen region we're updating, with no color attributes.
    We abstract it as a 2-d area, even if there's no actual chars printed at
    a particular location.
    '''
    def __init__(self, init_text=[]):
        ''' init_text: initializes the text content and virtual size of the area.
        The longest line establishes width.'''
        self._text = init_text
        self._width = max(self._text,key=len)



def main(win):
    with open('slinput.log','w') as keylog:
        keylog.write("--Log opened--\n")


        while True:
            try:
                pass
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

