import os

def cd(args):
    """
    カレントディレクトリを変更するコマンド
    """
    usageCode = "$ cd changeDirectoryPath"
    if len(args) < 2:
        print("Error : 引数が少なすぎます。")
        print("Usage :", usageCode)
        return 
    if len(args) > 3:
        print("Error : 引数が多すぎます。")
        print("Usage :", usageCode)
        return 

    
    os.chdir(args[1])

