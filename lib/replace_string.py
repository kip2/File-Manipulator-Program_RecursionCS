import os

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