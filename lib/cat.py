import os

def isPathFile(path):
    """
    ファイルパスがファイルであるかどうかを例外処理
    """
    # ディレクトリであるかどうかを判定
    if os.path.isdir(path):
        return "DIRECTORY"
    # ファイルであるかを判定
    if not os.path.isfile(path):
        return "NOT FILE"

def cat(args):
    """
    ファイルの内容を画面に表示する
    """

    usageCode = "$ " + "cat file1, file2, ..."
    if len(args) < 2:
        print("Error : 引数にファイルパスを指定してください。(1~)")
        print("Usage :", usageCode)
        return 

    for path in args[1:]:
        fileKind = isPathFile(path)
        if fileKind == "DIRECTORY":
            print("cat :", path, ": is a directory.")
        elif fileKind == "NOT FILE":
            print("cat :", path, ": is not a file")
        else:
            with open(path) as f:
                print(f.read())
            

