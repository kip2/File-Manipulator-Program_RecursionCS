import os

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
    
        