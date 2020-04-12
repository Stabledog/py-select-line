#!/usr/bin/env python3.8
# quiklog.py
import logging
import os
from datetime import datetime

class Quiklog:
    def __init__(self,main_logfile='/dev/null'):
        ''' Quiklog is a quick-and-dirty way to get logging that allows real-time
        monitoring of the log stream during development without jumping through too
        many hoops.

        1. Logs will be written to ./quiklog-9.log and flushed continually.  Calling
             process can redirect fd#9 to some other destination to change where that
             fast stream goes.  Messages written here do not get timestamps.
        2. Logs will also be written using the Python 'logging' module to 'main_logfile',
           unless it's /dev/null.  These logs get buffered, so they're slow to appear and
           most useful for production forensics outside the dev cycle.'''

        self.main_logfile = main_logfile if main_logfile != '/dev/null' else None
        self.quiklog_file='./quiklog-9.log'
        self.tty_fd=None
        self.is_tty=False

    def __enter__(self):
        try:
            os.fstat(9)  # Throws if fd 9 isn't open
            self.tty_fd = 9
            self.quiklog_file='/proc/self/fd/9'
        except:
            if os.path.isfile(self.quiklog_file):
                os.remove(self.quiklog_file)
            self.tty_fd = os.open(self.quiklog_file, os.O_WRONLY|os.O_CREAT)

        self.is_tty=os.isatty(self.tty_fd)
        self.write9(f"--- {datetime.now()} fast log opened in Log(), fd={self.tty_fd} ---")

        if self.main_logfile:
            logging.basicConfig(
                filename=self.main_logfile,
                level=logging.DEBUG,
                format='%(levelname)s:%(asctime)s %(message)s')
        return self

    def __exit__(self,type,value,traceback):
        os.close(self.tty_fd)

    def write9(self,msg,*args,**kwargs):
        ''' Writes directly to the fd#9 log only. '''
        os.write(self.tty_fd,f"{msg}\n".encode())
        if not self.is_tty:
            os.fsync(self.tty_fd)

    def debug(self,msg,*args,**kwargs):
        self.write9(f"debug: {msg}")
        if self.main_logfile:
            logging.debug(msg,args,kwargs)

    def info(self,msg,*args,**kwargs):
        self.write9(f"info: {msg}")
        if self.main_logfile:
            logging.info(msg,args,kwargs)

    def error(self,msg,*args,**kwargs):
        self.write9(f"error: {msg}")
        if self.main_logfile:
            logging.error(msg,args,kwargs)


if __name__ == "__main__":
    with Quiklog() as log:
        log.debug("This is a debug message")
        log.info("This is an info message")
        log.error("This is an error message")
