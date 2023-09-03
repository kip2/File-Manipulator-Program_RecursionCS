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
            'exit' : lib.exit,
            'cat' : lib.cat,
            'rm' : lib.rm,
            'mkdir' : lib.mkdir,
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
        cmd_line = input("> ")
        right_cmd_line = ""

        # redirect
        if  ">" in cmd_line:
            redirect_list = cmdline_split(cmd_line, ">")
            print("redirect_list:", redirect_list)
            # error処理
            if not canRedirect(redirect_list):
                print("redirect error")
                continue
            # 暫定でリスト0の値のみsplit
            # [1]の値も渡さないといけない
            cmd_line = redirect_list[0]
            right_cmd_line = redirect_list[1].lstrip()

        print("parsed_redirect_list:", cmd_line) 
        print("right_list:", right_cmd_line) 

        # pipe
        """
        pipeはリストになる予定なので、配列のそれぞれの要素に対してsplitして、コマンドがあるかどうかを確かめて動作させないといけない
        """
        if "|" in cmd_line:
            pipe_list = cmdline_split(cmd_line, "|") 
            print("pipe_list:", cmd_line)
            # error処理
            if not canPipe(pipe_list):
                print("pipe error")
                continue

        user_input_args_list = cmd_line.split()

        # 例外処理
        if len(user_input_args) == 0:
            continue
        for i in range(len(user_input_args_list)):
            user_input_args = user_input_args_list[i]
            # テストコード用
            if user_input_args[0].lower() == "test":
                testCommand(user_input_args)
                # テストなのでループをせずに終了する
                COMMANDS["exit"](user_input_args)
            # 通常処理
            else:
                evalCommand(user_input_args)

def cmdline_split(cmdline, str):
    arr = cmdline.split(str)
    return lstripArray(arr)

def canPipe(pipe_list):
    for i in range(len(pipe_list)):
        if not pipe_list.split(" ")[0] in COMMANDS:
            return False
    return True

def lstripArray(arr):
    """
    配列の要素それぞれの、先頭のスペースを除く
    """
    # 空のリストなら空のリストを返す
    if len(arr) == 0: return []

    for i in range(len(arr)):
        arr[i] = arr[i].lstrip()
    return arr

def canRedirect(redirect_list):
    # 何も記述がないならerror
    if redirect_list[1].replace(" ", "") == "":
        return False

    # todo: 2と1とが出力先としている
    return True
        
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

if __name__ == "__main__":
    prologue()
    inputLoop()

