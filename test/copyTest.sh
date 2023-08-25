#!/bin/bash

# testcase
inputFile="./copy/input.txt"
outputFile="./copy/output.txt"
inputFile2="./copy/input2.txt"
outputFile2="./copy/output2.txt"

# pathcase
pathOutputFile="./copy/pathCase/output.txt"
pathOutputFile2="./copy/pathCase/output2.txt"

testEcho="""
        test
        copy
        copy aaa
        copy aaa bbb
        copy aaa bbb ccc
        copy $inputFile $outputFile
        copy $inputFile2 $outputFile2
        "

exitCommand="exit"

echo $testEcho $exitCommand| python3 ../file_manipulator.py

# asset
echo "******* assert ********"
echo $outputFile $pathOutputFile
diff $outputFile $pathOutputFile
if [ $? -eq 0 ]; then
    echo "同じファイルです。"
elif [ $? -eq 1 ]; then
    echo "違うファイルです。"
fi
echo $outputFile2 $pathOutputFile2
diff $outputFile2 $pathOutputFile2
if [ $? -eq 0 ]; then
    echo "同じファイルです。"
elif [ $? -eq 1 ]; then
    echo "違うファイルです。"
fi
