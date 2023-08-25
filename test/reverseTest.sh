#!/bin/bash

# testcase
inputFile="./reverse/input.txt"
outputFile="./reverse/output.txt"
inputFile2="./reverse/input2.txt"
outputFile2="./reverse/output2.txt"

# pathcase
pathOutputFile="./reverse/pathCase/output.txt"
pathOutputFile2="./reverse/pathCase/output2.txt"

testEcho="""
        test
        reverse
        reverse aaa
        reverse aaa bbb
        reverse aaa bbb ccc
        reverse $inputFile $outputFile
        reverse $inputFile2 $outputFile2
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
