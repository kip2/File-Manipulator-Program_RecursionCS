#!/bin/bash
testEcho="reverse\n"

exitCommand="exit"

echo $testEcho $exitCommand| python3 ../file_manipulator.py
