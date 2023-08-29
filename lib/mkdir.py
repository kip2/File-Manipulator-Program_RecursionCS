import os

def isPathExists(path):
    """
    ファイルパスにファイルがあるかどうかを確認
    """
    # ディレクトリであるかどうかを判定
    if os.path.exists(path):
        return True
    return False

def mkdir(args):
    """
    指定されたファイルパスにディレクトリを作る
    """

    usageCode = "$ " + "mkdir file1, file2, ..."
    if len(args) < 2:
        print("Error : 引数にファイルパスを指定してください。(1~)")
        print("Usage :", usageCode)
        return 

    for path in args[1:]:
        if isPathExists(path):
            print("mkdir :", path, ": File exitsts.")
        else:
            os.mkdir(path)
            

