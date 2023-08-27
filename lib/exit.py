import sys
import os

def exit(args):
    """
    カレントディレクトリを変更するコマンド
    """
    usageCode = "$ " + "exit"
    if len(args) > 2:
        print("Error : 引数が多すぎます。")
        print("Usage :", usageCode)
        return 

    print("Bye!!!")
    sys.exit()
