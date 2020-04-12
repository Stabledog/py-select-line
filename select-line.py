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
from dataclasses import dataclass
import sys
import os
from quiklog import Quiklog

with Quiklog() as logger:

    @dataclass
    class Position:
        x = int
        y = int

    @dataclass
    class Model:
        input_text = []
        candidate_string = str
        cursor_pos = Position()

    class EventLoop:
        def __init__(self,terminal):
            self.terminal = terminal
            self.keymap={}
            ''' The keymap associates key events with handlers '''

        def run(self):
            term = self.terminal
            with term.cbreak():
                val = ''
                while True:
                    val = term.inkey(timeout=1)
                    # type(val) is "blessed.keyboard.Keystroke"
                    if not val:
                        self.pump_events()
                        val = ''
                        continue
                    elif val.is_sequence:
                        logger.info(f"key sequence: {val},{val.name},{val.code}")
                    else:
                        logger.info(f"key: {val}")
                    kval=val.__repr__()
                    if kval in self.keymap:
                        logger.info(f"key {kval} has a handler, dispatching:")
                        self.keymap[kval](kval)
                logger.info("Quit received from key input")

        def pump_events(self):
            pass

        def add_handler(self, keystroke, handler):
            ''' Add a blessed.keyboard.Keystroke handler.
            The 'keystroke' is a string as produced by 'key.__repr__()' '''
            self.keymap[keystroke] = handler

    def main(win):
        with open('slinput.log','w') as keylog:
            keylog.write("--Log opened--\n")
            while True:
                try:
                    pass
                except Exception :
                    # No input
                    pass


    if __name__ == "__main__":
        liststream=sys.stdin
        try:
            log(f"sys.argv={sys.argv}")
            if os.path.isfile(sys.argv[1]):
                liststream = open( sys.argv[1], 'r')
        except:
            pass

        items = liststream.read().split('\n')
        model = Model(items)

        main(items)

