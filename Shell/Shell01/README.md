# Shell 01

## English

Shell exercises for inspecting user information and files and displaying selected results. Commands are combined to extract filenames, count entries, and display network information.

For example, `find_sh.sh` finds `.sh` files beneath its working directory and prints their names without extensions. Exercises `ex01` through `ex06` are included.

### Scripts

| File | Behavior |
| --- | --- |
| [ex01/print_groups.sh](ex01/print_groups.sh) | List groups for the user named by `FT_USER` |
| [ex02/find_sh.sh](ex02/find_sh.sh) | Find .sh files and print names without extensions |
| [ex03/count_files.sh](ex03/count_files.sh) | Count entries below the current directory |
| [ex04/MAC.sh](ex04/MAC.sh) | Extract MAC addresses from ifconfig output |
| [ex05](ex05/) | Practice a filename containing symbols; the file contains `42` |
| [ex06/skip.sh](ex06/skip.sh) | Print every other line of ls output |

### Examples

Run from this directory. `FT_USER` is the username whose groups you want to inspect.

```sh
FT_USER="$(id -un)" sh ex01/print_groups.sh
sh ex02/find_sh.sh
sh ex03/count_files.sh
```

`ex04/MAC.sh` requires `ifconfig` output containing `ether` lines.

`make` checks script syntax; `make run` runs `ex02/find_sh.sh`. Set `SCRIPT` to select another script.

## 日本語

ユーザー情報やファイルを調べ、必要な部分だけを表示するShell演習です。複数のコマンドをつなぎ、ファイル名の抽出、項目数の集計、ネットワーク情報の表示などを行います。

例えば `find_sh.sh` は、実行した場所の下にある `.sh` ファイルを探し、拡張子を取り除いた名前を表示します。`ex01`〜`ex06` の演習を収録しています。

### スクリプト

| ファイル | 動作 |
| --- | --- |
| [ex01/print_groups.sh](ex01/print_groups.sh) | `FT_USER` で指定したユーザーのグループ一覧 |
| [ex02/find_sh.sh](ex02/find_sh.sh) | .shファイルを検索し、拡張子を除いた名前を表示 |
| [ex03/count_files.sh](ex03/count_files.sh) | 現在のディレクトリ以下の項目数を表示 |
| [ex04/MAC.sh](ex04/MAC.sh) | ifconfigの出力からMACアドレスを抽出 |
| [ex05](ex05/) | 記号を含むファイル名を扱う演習。内容は `42` |
| [ex06/skip.sh](ex06/skip.sh) | lsの出力を1行おきに表示 |

### 実行例

このディレクトリで実行します。`FT_USER` はグループを調べるユーザー名です。

```sh
FT_USER="$(id -un)" sh ex01/print_groups.sh
sh ex02/find_sh.sh
sh ex03/count_files.sh
```

`ex04/MAC.sh` は `ifconfig` と、その出力に含まれる `ether` 行を使います。

`make` でスクリプトの構文を確認し、`make run` で `ex02/find_sh.sh` を実行できます。`SCRIPT` で別のスクリプトを選べます。
