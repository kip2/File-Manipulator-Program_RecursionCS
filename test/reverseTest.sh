#!/bin/bash
testEcho="""
        test
        reverse
        reverse aaa
        reverse aaa bbb
        reverse aaa bbb ccc
        "

exitCommand="exit"

echo $testEcho $exitCommand| python3 ../file_manipulator.py
