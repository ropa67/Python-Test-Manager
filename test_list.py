#!/usr/bin/env python
# -*- coding: utf8 -*-

import os, glob

def list_tests():
    os.chdir("test_runs")  # change a dir
    filelist = glob.glob("*.xml")  # reading the fail list

    print"""
    ********************************
         LIST OF TEST STARTS
    ********************************
    """
    for f in filelist:                   # list of file names displayed by a loop, strim - deleted a .xml
        item = f.strip('.xml')
        print("\t" + item)
    print"""
    ********************************
    """
    os.chdir("..")
    raw_input("Press [Enter]:  ")
