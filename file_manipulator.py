import os
import lib

def prologue():
    """
    file manipulatorの起動画面
    """
    titleLogo = """
====================================
************************************

                FILE
            MANIPULATOR

************************************
====================================
"""
    print(titleLogo)

def inputLoop():
    """
    インプットを処理する関数
    """
    while True:
        print("> ", end="")
        userInputArgs = input().split()

        # 例外処理
        if len(userInputArgs) == 0:
            continue
        # 終了処理
        elif userInputArgs[0].lower() == "exit":
            return
        # テストコード用
        elif userInputArgs[0].lower() == "test":
            testCommand(userInputArgs)
            return 
        # 通常処理
        else:
            evalCommand(userInputArgs)
        
def evalCommand(args) :
    """
    インプットから得られたコマンドを処理する関数
    """
    # 第1引数のコマンドを評価し、コマンドを実行する
    match args[0]:
        case "reverse":
            lib.reverse(args)
        case "copy":
            lib.copy(args)
        case "duplicate-contents":
            lib.duplicateContents(args)
        case "replace-string":
            replaceString(args)
        case _:
            print("そのようなコマンドは存在しません。")

def testCommand(args):
    """
    コマンドのテスト用
    Usage: test
    以上のコマンドを入力すると、テスト入力待ち状態になる
    主にシェルスクリプト用
    """
    print("******* test case **********")
    while True:
        userTestInputArgs = input().split()
        print(">", " ".join(userTestInputArgs))
        if userTestInputArgs[0].lower() == "exit":
            return
        else:
            evalCommand(userTestInputArgs)


def replaceString(args):
    """
    replace-string コマンド
    Usage: replace-string inputpath needle newstring
    inputpathにあるファイルの内容から文字列'needle'を検索し、'needle'の全てを'newstring'に置き換える
    """
    # 引数の数のエラー処理
    usageCode = "$ replace-string inputpath needle newstring"
    if len(args) == 1:
        print("Error : インプットファイルと置換文字列が未入力です。")
        print("Usage :", usageCode)
        return 
    elif len(args) == 2:
        print("Error : 置換文字列が未入力です。")
        print("Usage :", usageCode)
        return 
    elif len(args) == 3:
        print("Error : 置換後の文字列が未入力です。")
        print("Usage :", usageCode)
        return 
    elif len(args) > 4:
        print("Error : 引数が多すぎます。")
        print("Usage :", usageCode)
        return 

    inputpathName = args[1]
    needle = args[2]
    newString = args[3]
    
    if os.path.isfile(inputpathName):
        # inputファイル読み込み
        with open(inputpathName) as f:
            replaceContents = f.read()
        # inputパスに置換後のファイルを上書きする
        with open(inputpathName, "w") as f:
            f.write(replaceContents.replace(needle, newString))
    else:
        print("インプットパスにファイルが存在しません。")

def epilogue():
    """
    終了処理
    """
    print("Bye!")

if __name__ == "__main__":
    prologue()
    inputLoop()
    epilogue()

