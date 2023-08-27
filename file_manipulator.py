import lib
import readline

# 実行可能コマンド群
COMMANDS = {'reverse': lib.reverse, 
            'copy': lib.copy, 
            'duplicate-contents': lib.duplicateContents,
            'replace-string': lib.replaceString,
            'pwd': lib.pwd,
            'cd': lib.cd,
            'ls' : lib.ls,
            'whoami' : lib.whoami,
            }

def tabCompletion():
    """
    Tabキーによるコマンド補完
    """
    def complete(text, state):
        for cmd in COMMANDS:
            if cmd.startswith(text):
                if not state:
                    return cmd
                else:
                    state -= 1

    readline.parse_and_bind("tab: complete")
    readline.set_completer(complete)


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

    # tabキーによる補完機能追加
    tabCompletion()
    
    # ｍain loop
    while True:
        userInputArgs = input("> ").split()

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
    if args[0] in COMMANDS:
        COMMANDS[args[0]](args)
    else:
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

def epilogue():
    """
    終了処理
    """
    print("Bye!")

if __name__ == "__main__":
    prologue()
    inputLoop()
    epilogue()

