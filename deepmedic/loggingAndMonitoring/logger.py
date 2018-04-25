# Copyright (c) 2016, Konstantinos Kamnitsas
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the BSD license. See the accompanying LICENSE file
# or read the terms at https://opensource.org/licenses/BSD-3-Clause.

from __future__ import absolute_import, print_function, division
import datetime


class Logger :
    loggerFileName = None
    
    def print3(self, string) :
        print(string)    
        f = open(self.loggerFileName,'a')
        f.write(str(datetime.datetime.now())+" >> "+string+"\n")
        f.close()
        
    def __init__(self, filenameAndPathOfLoggerTxt="logs/defaultLogFile.txt") :
        self.loggerFileName = filenameAndPathOfLoggerTxt
        self.print3("=============================== logger created =======================================")
        