#!/bin/bash

# testcase
inputFile="./duplicate-contents/input.txt"
inputFile2="./duplicate-contents/input2.txt"

# pathcase
pathInputFile="./duplicate-contents/pathCase/input.txt"
pathInputFile2="./duplicate-contents/pathCase/input2.txt"

testEcho="""
        test
        duplicate-contents
        duplicate-contents aaa
        duplicate-contents aaa bbb
        duplicate-contents aaa bbb ccc
        duplicate-contents $inputFile 5
        duplicate-contents $inputFile c
        duplicate-contents $inputFile2 2
        duplicate-contents $inputFile2 b
        "

exitCommand="exit"

echo $testEcho $exitCommand| python3 ../file_manipulator.py

# asset
echo "******* assert ********"
echo $inputFile $pathInputFile
diff $inputFile $pathInputFile
if [ $? -eq 0 ]; then
    echo "同じファイルです。"
elif [ $? -eq 1 ]; then
    echo "違うファイルです。"
fi
echo $inputFile2 $pathInputFile2
diff $inputFile2 $pathInputFile2
if [ $? -eq 0 ]; then
    echo "同じファイルです。"
elif [ $? -eq 1 ]; then
    echo "違うファイルです。"
fi
