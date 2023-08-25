#!/bin/bash

# testcase
inputFile="./replace-string/input.txt"
inputFile2="./replace-string/input2.txt"

# pathcase
pathInputFile="./replace-string/pathCase/input.txt"
pathInputFile2="./replace-string/pathCase/input2.txt"

testEcho="""
        test
        replace-string
        replace-string aaa
        replace-string aaa bbb
        replace-string aaa bbb ccc
        replace-string aaa bbb ccc ddd
        replace-string $inputFile needle newstring
        replace-string $inputFile2 Alice Bob
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

rm $inputFile
rm $inputFile2
cp ./replace-string/originalFile/input.txt ./replace-string
cp ./replace-string/originalFile/input2.txt ./replace-string