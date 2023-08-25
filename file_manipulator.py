def prologue():
    """
    file manipulatorの起動画面
    """
    titleLogo = """
********************************************************************
********************************************************************
********************************************************************
      ■                                                          
  ■■■■■ ■■ ■                                                     
  ■        ■                                                     
  ■     ■  ■  ■■■                                                
  ■■■■■ ■  ■ ■   ■                                               
  ■     ■  ■ ■■■■■                                               
  ■     ■  ■ ■                                                   
  ■     ■  ■ ■   ■                                               
  ■     ■  ■  ■■■■                                               
                                                                 
  ■      ■                                                       
  ■      ■              ■■              ■■        ■              
  ■■    ■■                              ■■        ■              
  ■■    ■■  ■■■■  ■■■■■ ■■ ■■■■■  ■   ■ ■■ ■■■■ ■■■■  ■■■■  ■■■ ■
  ■ ■  ■ ■  ■  ■  ■■  ■ ■■ ■■  ■  ■   ■ ■■ ■   ■  ■  ■■  ■■ ■    
  ■ ■  ■ ■   ■■■  ■   ■ ■■ ■   ■■ ■   ■ ■■  ■■■■  ■  ■   ■■ ■    
  ■ ■■ ■ ■  ■  ■  ■   ■ ■■ ■   ■■ ■   ■ ■■ ■   ■  ■  ■    ■ ■    
  ■  ■■  ■  ■  ■■ ■   ■ ■■ ■■  ■  ■   ■ ■■ ■  ■■  ■  ■■  ■■ ■    
  ■  ■■  ■  ■■■■■ ■   ■ ■■ ■ ■■■  ■■■■■ ■■ ■■■■■  ■■  ■■■■  ■    
                           ■                                     
                           ■                           
********************************************************************
********************************************************************
********************************************************************
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
        else:
            evalCommand(userInputArgs)
        
def evalCommand(args) :
    """
    インプットから得られたコマンドを処理する関数
    """

    # 第1引数を評価し、各々のコマンドを実行する
    match args[0]:
        case "reverse":
            print("reverse")
        case "copy":
            print("copy")
        case "duplicate-contents":
            print("duplicate-contents")
        case "replace-string":
            print("replace-string")

def reverse():
    """
    reverse コマンド
    Usage: reverse inputpath outputpath
    inputpathにあるファイルを受け取り、outputpathに、inputpathの内容を逆にした新しいファイルを作成
    """
    pass

def copy():
    """
    copy コマンド
    Usage: copy inputpath outputpath
    inputpathになるファイルのコピーを作成し、outputpathとして保存する
    """
    pass

def duplicateContents():
    """
    duplicate-contents コマンド
    Usage : duplicate-contents inputpath n
    inputpathにあるファイルの内容を読み込み、その内容を複製し、複製された内容をinputpathにn回繰り返して保存
    """
    pass

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
    print("By!")

if __name__ == "__main__":
    prologue()
    inputLoop()
    epilogue()

