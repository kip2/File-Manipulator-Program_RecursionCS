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
        elif userInputArgs[0].lower() == "test":
            testCommand(userInputArgs)
            return 
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
            print("copy")
        case "duplicate-contents":
            print("duplicate-contents")
        case "replace-string":
            print("replace-string")

def reverse(args):
    """
    reverse コマンド
    Usage: reverse inputpath outputpath
    inputpathにあるファイルを受け取り、outputpathに、inputpathの内容を逆にした新しいファイルを作成
    """
    if len(args) == 1:
        print("Error : インプットファイルとアウトプットパスが未入力です。")
        print("Usage : $ reverse inputpath outputpath")
    elif len(args) == 2:
        print("Error : アウトプットパスが未入力です。")
        print("Usage : $ reverse inputpath outputpath")
    elif len(args) > 3:
        print("Error : 引数が多すぎます。")
        print("Usage : $ reverse inputpath outputpath")
        
def testCommand(args):
    # test用
    print("******* test case **********")
    while True:
        userTestInputArgs = input().split()
        print(">", " ".join(userTestInputArgs))
        if userTestInputArgs[0].lower() == "exit":
            return
        else:
            evalCommand(userTestInputArgs)

        

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
    print("Bye!")

if __name__ == "__main__":
    prologue()
    inputLoop()
    epilogue()

