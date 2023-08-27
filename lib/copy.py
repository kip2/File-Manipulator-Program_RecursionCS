import os

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