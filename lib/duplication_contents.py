import os

def duplicateContents(args):
    """
    duplicate-contents コマンド
    Usage : duplicate-contents inputpath n
    inputpathにあるファイルの内容を読み込み、その内容を複製し、複製された内容をinputpathにn回繰り返して保存
    """

    # 引数の数のエラー処理
    usageCode = "$ duplicate-contents inputpath n"
    if len(args) == 1:
        print("Error : インプットファイルと数字が未入力です。")
        print("Usage :", usageCode)
        return 
    elif len(args) == 2:
        print("Error : 数字が未入力です。")
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