## py-select-line taskrc.md
`select-line` is a Python script that serves as smarter replacement for the crummy `bash select` built-in.

### Dependencies
  - Requires the [blessed](https://github.com/jquast/blessed) package


### Usage:
    select-line --list [filename] {--default-row NN} {--print-full}

    Prints list and then provides a keystroke UI for quick matching of entries.

    Output:
        - (default) Prints the selected key on stdout when complete.
        - `--print-full` Prints the entire row of match
    Returns:
         non-zero if user cancel or error

### Example
```bash
function do_example {
    local choice=$(select-line --default-row 1 --list \
        <( ls *cpp | cat -n ; echo 'C cancel <ESC>'; echo '(Enter) default'))
    if [[ $choice == 'C' ]]; then  # user cancelled
        echo "..."
    else
        # User chose a file and 'choice' is the row number of that file
        echo "..."
    fi
}
```
## Development notes:
readline integration: https://pymotw.com/2/readline/

```bash
#= = = = = = = = = = =

appargs=
#appargs=test/test1.lst
python=$(which python3.8 python3.7 python3.6 | head -n 1)
scr=select-line.py
dbgport=5679
function debug_one {
    #Help
    clear
    echo "debug() waiting in $PWD for debugger attach on 0.0.0.0:$dbgport..."
    $python -m ptvsd --host 0.0.0.0 --port $dbgport --wait $scr $appargs $@
    stty sane
}

function run_one {
    #Help
    xtty=$(cat .diagloop-tty)
    echo "diag xtty=${xtty}"
    local cmd="$python $scr $appargs $@"
    echo "Running: $cmd" >&2
    $cmd 9>${xtty}
}

function vscode_sh_init {
    echo "::: Run dev-loop for debugging and testing. :::"
    dev-loop
}



```
