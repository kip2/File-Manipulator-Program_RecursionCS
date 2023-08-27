import os

def ls(args):
    """
    カレントディレクトリを変更するコマンド
    """
    usageCode = "$ " + "ls"
    if len(args) > 2:
        print("Error : 引数が多すぎます。")
        print("Usage :", usageCode)
        return 

    for file in sorted(os.listdir()):
        print(file)

