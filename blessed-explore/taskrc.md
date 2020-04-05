## taskrc.md for blessed-explore

Any markdown content can live here.  Embedded bash code blocks can be included,
they will be injected into the shell. Run `taskrc -h` for more.

```bash

function debug {
    #Help
    python3.7 -m pudb ./blessed-explore.py "$@"
}

function run {
    python3.7 ./blessed-explore.py "$@"
}

```
