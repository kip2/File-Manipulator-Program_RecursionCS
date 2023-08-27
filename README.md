# File-Manipulator-Program_RecursionCS

## 概要

RecursionCS( https://recursionist.io )で作ったBackend Projectの課題作品です。

幾つかのコマンドが打てる簡単なターミナルシェルです。

用意されているコマンドは以下。(課題要件の範囲)

- reverse : ファイルの文字列をひっくり返して、別ファイルに保存するコマンド。
- copy : ファイルのコピーを作成し、保存するコマンド。
- duplicate-contents : ファイルの内容をn回複製して元のファイルに統合するコマンド。
- replace-string : ファイルの全ての文字列を置換するコマンド。

以下はその後、追加したコマンドです。
- pwd : カレントディレクトリを表示するコマンド。
- cd : カレントディレクトリを変更するコマンド。
  

--- 

## 使い方

pythonスクリプトですので、ターミナル上で作業をしてください。

1. ターミナルに以下のコマンドを入力する。

```shell
$ python3 file_manipulator.py
```

2. REPLが立ち上がるので、コマンドを入力する。

※TABキーによるコマンド補完機能が使えます。コマンドが曖昧な場合でも安心です。

### 各コマンドの使い方

#### reverse

inputpathにあるファイルを開き、outputpathにinputpathの内容を逆にした新しいファイルを作成します。

```plain
> reverse inputpath outputpath
```

#### copy

inputpthにあるファイルのコピーを作成し、outputpathにコピーを保存します。

```plain
> copy inputpath outputpath
```

#### duplicate-contents

inputpathにあるファイルの内容をnで指定された回数複製し、複製された内容をinputpathに上書きして保存します。

```plain
> duplicate-contents inputpath n
```

#### replace-string

inputpathにあるファイル全体の文字列を置換します。

例）ファイル全体の'needle'を'newstring'に置換する。

```plain
> replace-string inputpath needle newstring
```

and more...

--- 

## 見てほしいところ

- 課題要件ですが、引数の数が適正か判定するバリデーションを組み込んでいます。
- シェルスクリプトの練習のため、簡単なテストスクリプトを自前で組んで行っています。テストにより、ある程度の動作は保証されていると思います。
- Tabキーによるコマンド補完機能を追加しています。
- 拡張性を高めるため、コマンドを外部ファイルにしてimportしています。また、コマンドと該当の関数を辞書に登録して管理しています。

## 変更

ver1.11: pwd, cdコマンドを追加。

ver 1.1 : Tabキーによるコマンド補完機能を追加。

ver 1.0 : reverse, copy, duplicate-contents, replace-stringを実装。