import os

def whoami(args):
    """
    カレントディレクトリを変更するコマンド
    """
    usageCode = "$ " + "whoami"
    if len(args) > 2:
        print("Error : 引数が多すぎます。")
        print("Usage :", usageCode)
        return 

    print(os.getlogin())
