import os

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
            reverse(args)
        case "copy":
            copy(args)
        case "duplicate-contents":
            duplicateContents(args)
        case "replace-string":
            print("replace-string")
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


def reverse(args):
    """
    reverse コマンド
    Usage: reverse inputpath outputpath
    inputpathにあるファイルを受け取り、outputpathに、inputpathの内容を逆にした新しいファイルを作成
    """
    # 引数の数のエラー処理
    usageCode = "$ reverse inputpath outputpath"
    if len(args) == 1:
        print("Error : インプットファイルとアウトプットパスが未入力です。")
        print("Usage :", usageCode)
        return 
    elif len(args) == 2:
        print("Error : アウトプットパスが未入力です。")
        print("Usage :", usageCode)
        return 
    elif len(args) > 3:
        print("Error : 引数が多すぎます。")
        print("Usage :", usageCode)
        return 
    
    inputpathName = args[1]
    outputpathName = args[2]

    if os.path.isfile(inputpathName):
        # inputファイル読み込み
        with open(inputpathName) as f:
            contents = f.read()
            writeContents = contents[::-1]
        # outputパスにファイルを書き出す
        with open(outputpathName, "w") as f:
            f.write(writeContents)
    else:
        print("インプットパスにファイルが存在しません。")
    
        

def copy(args):
    """
    copy コマンド
    Usage: copy inputpath outputpath
    inputpathになるファイルのコピーを作成し、outputpathとして保存する
    """
    # 引数の数のエラー処理
    usageCode = "$ copy inputpath outputpath"
    if len(args) == 1:
        print("Error : インプットファイルとアウトプットパスが未入力です。")
        print("Usage :", usageCode)
        return 
    elif len(args) == 2:
        print("Error : アウトプットパスが未入力です。")
        print("Usage :", usageCode)
        return 
    elif len(args) > 3:
        print("Error : 引数が多すぎます。")
        print("Usage :", usageCode)
        return 
    
    inputpathName = args[1]
    outputpathName = args[2]

    if os.path.isfile(inputpathName):
        # inputファイル読み込み
        with open(inputpathName) as f:
            writeContents = f.read()
        # outputパスにファイルを書き出す(コピー)
        with open(outputpathName, "w") as f:
            f.write(writeContents)
    else:
        print("インプットパスにファイルが存在しません。")

def duplicateContents(args):
    """
    duplicate-contents コマンド
    Usage : duplicate-contents inputpath n
    inputpathにあるファイルの内容を読み込み、その内容を複製し、複製された内容をinputpathにn回繰り返して保存
    """

    # 引数の数のエラー処理
    usageCode = "$ duplicate-contents inputpath n"
    if len(args) == 1:
        print("Error : インプットファイルとアウトプットパスが未入力です。")
        print("Usage :", usageCode)
        return 
    elif len(args) == 2:
        print("Error : アウトプットパスが未入力です。")
        print("Usage :", usageCode)
        return 
    elif len(args) > 3:
        print("Error : 引数が多すぎます。")
        print("Usage :", usageCode)
        return 

    # 数字が指定されているかのエラー処理
    if not args[2].isnumeric():
        print("Error : 第2引数には数字を入力してください。")
        print("Usage :", usageCode)
        return

    inputpathName = args[1]

    n = int(args[2])

    if os.path.isfile(inputpathName):
        # inputファイル読み込み
        with open(inputpathName) as f:
            writeContents = f.read()
        # inputパスにファイルの内容を複製する
        with open(inputpathName, "a") as f:
            for i in range(n):
                f.write('\n'+writeContents)
    else:
        print("インプットパスにファイルが存在しません。")

def replaceString():
    """
    replace-string コマンド
    Usage: replace-string inputpath needle newstring
    inputpathにあるファイルの内容から文字列'needle'を検索し、'needle'の全てを'newstring'に置き換える
    """
    pass

def epilogue():
    """
    終了処理
    """
    print("Bye!")

if __name__ == "__main__":
    prologue()
    inputLoop()
    epilogue()

