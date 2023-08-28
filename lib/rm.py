import os

def isPathDirectory(path):
    """
    パス先のファイルがディレクトリであるかどうか判定
    """
    if os.path.isdir(path):
        return True
    return False

def rm(args):
    """
    ファイルの内容を画面に表示する
    """

    usageCode = "$ " + "rm file1, file2, ..."
    if len(args) < 2:
        print("Error : 引数にファイルパスを指定してください。(1~)")
        print("Usage :", usageCode)
        return 

    for path in args[1:]:
        if isPathDirectory(path):
            print("rm: ", path, ":", "is a directory")
        else:
            os.remove(path)
