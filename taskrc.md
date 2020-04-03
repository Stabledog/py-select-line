## py-select-line taskrc.md
`select-line` is a Python script that serves as curses-based smart replacement for the crummy `bash select` built-in.

### TODO
 - http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html


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

```bash
appargs="./select-line.py test/test1.lst"

function debug {
    #Help
    [[ -z $PUDB_TTY ]] && return $(errExit PUDB_TTY not defined)
    echo "Debugger on $PUDB_TTY: in case of trouble, run 'sleep 100000' on that \
        terminal before launching debug."

    python3.7 -m pudb $appargs
}

function run {
    #Help To write logs to another terminal, do 'ln -sf /dev/my/tty/other ./slinput.log'
    python3.7 $appargs
}

function tail_log {
    #Help To write to another terminal, do 'ln -sf /dev/my/tty/other ./slinput.log'
    touch slinput.log
    tail -f slinput.log
}
```
