import os

def pwd(args):
    """
    カレントディレクトリを表示するコマンド
    """
    usageCode = "$ pwd"
    if len(args) > 2:
        print("Error : 引数が多すぎます。")
        print("Usage :", usageCode)
        return 

    print(os.getcwd())