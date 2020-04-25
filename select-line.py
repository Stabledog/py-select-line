# Requires python3.7 or greater
#
#  Given a list of items on stdin, display them on stderr and
#  then read keystrokes from the user to match the items.
#  Upon selection, print the entire line selected to stdout.
#
#  The first column is a key field: an exact match from user entry
#  will cause immediate completion without ENTER.

#  Because select-line doesn't output to stdout until completion, it
#  is easy to use from subshells in command substitution contexts.

from  blessed  import Terminal # See https://blessed.readthedocs.io/en/latest/api/terminal.html
from dataclasses import dataclass
import sys
import os
from quiklog import Quiklog
import readline

logger = None

@dataclass
class Position:
    x = int
    y = int



class InputLoop:
    def __init__(self):
        pass

    def run(self):
        while True:
            try:
                val = input()
            except EOFError:
                break
            # type(val) is "blessed.keyboard.Keystroke"
            if not val:
                continue
            logger.debug(f"input() returns: {val}")
            print(val)
            break



@dataclass
class Model:
    input_text = []
    candidate_string = str
    cursor_pos = Position()

    def __init__(self,input_text):
        self.input_text=input_text

@dataclass
class Renderer:
    def __init__(self,terminal,model):
        self.model = model
        self.terminal = terminal
        self.screen_origin = terminal.location()
        ''' screen_origin is the logical 0,0 for the region we render,
        containing the screen-space coordinates of the upper-left corner '''

    def render(self):
        for line in self.model.input_text:
            print(line)

class App:
    ''' Top-level behavioral management '''
    def __init__(self, model, terminal, event_loop, renderer):
        self.model = model
        self.terminal = terminal
        self.event_loop = event_loop
        self.renderer = renderer

    def run(self):
        self.event_loop.run()

if __name__ == "__main__":
    with Quiklog() as lg:
        logger = lg
        liststream=sys.stdin
        logger.info(f"sys.argv={sys.argv}")
        try:
            if os.path.isfile(sys.argv[1]):
                liststream = open( sys.argv[1], 'r')
                logger.debug(f"Input loaded from ${sys.argv[1]}")
        except:
            pass
        items = liststream.read().split('\n')
        if len(items)==0:
            sys.exit("ERROR: no list items provided to select-line.py\n")

        logger.debug(f"{len(items)} items defined in input")
        model = Model(items)
        terminal = Terminal()
        input_loop = InputLoop()
        renderer = Renderer(terminal,model)
        renderer.render()
        app = App(model, terminal, input_loop, renderer)
        app.run()









