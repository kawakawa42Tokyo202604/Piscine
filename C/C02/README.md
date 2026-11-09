# Piscine C 02

## English

C exercises in copying strings, checking their characters, and changing letter case. Each function processes a string character by character.

For example, `ft_strupcase` changes `Hello` to `HELLO`. The memory-display exercise `ex12` is not implemented.

### Exercises

| Location | Source | Behavior |
| --- | --- | --- |
| ex00 | [ft_strcpy.c](ex00/ft_strcpy.c) | Copy a string |
| ex01 | [ft_strncpy.c](ex01/ft_strncpy.c) | Copy a specified number of characters |
| ex02 | [ft_str_is_alpha.c](ex02/ft_str_is_alpha.c) | Check for letters only |
| ex03 | [ft_str_is_numeric.c](ex03/ft_str_is_numeric.c) | Check for digits only |
| ex04 | [ft_str_is_lowercase.c](ex04/ft_str_is_lowercase.c) | Check for lowercase only |
| ex05 | [ft_str_is_uppercase.c](ex05/ft_str_is_uppercase.c) | Check for uppercase only |
| ex06 | [ft_str_is_printable.c](ex06/ft_str_is_printable.c) | Check for printable characters |
| ex07 | [ft_strupcase.c](ex07/ft_strupcase.c) | Convert to uppercase |
| ex08 | [ft_strlowcase.c](ex08/ft_strlowcase.c) | Convert to lowercase |
| ex09 | [ft_strcapitalize.c](ex09/ft_strcapitalize.c) | Capitalize words |
| ex10 | [ft_strlcpy.c](ex10/ft_strlcpy.c) | Copy within destination capacity |
| ex11 | [ft_putstr_non_printable.c](ex11/ft_putstr_non_printable.c) | Display nonprintable characters in hexadecimal |
| ex12 | [ft_print_memory.c](ex12/ft_print_memory.c) | Display memory; not implemented |

### Compile an example

Use a C compiler from this directory.

```sh
cc -Wall -Wextra -Werror -c ex00/ft_strcpy.c -o ft_strcpy.o
```

This creates an object file. To run the function, link its source with a `main.c` that calls it.

## 日本語

文字列をコピーしたり、含まれる文字を調べたり、大文字・小文字を変換したりするC演習です。文字列を1文字ずつたどって処理します。

例えば `ft_strupcase` は `Hello` を `HELLO` に変えます。メモリの内容を表示する `ex12` は未実装です。

### 演習

| 場所 | ソース | 処理 |
| --- | --- | --- |
| ex00 | [ft_strcpy.c](ex00/ft_strcpy.c) | 文字列をコピー |
| ex01 | [ft_strncpy.c](ex01/ft_strncpy.c) | 文字数を指定してコピー |
| ex02 | [ft_str_is_alpha.c](ex02/ft_str_is_alpha.c) | 英字だけかを判定 |
| ex03 | [ft_str_is_numeric.c](ex03/ft_str_is_numeric.c) | 数字だけかを判定 |
| ex04 | [ft_str_is_lowercase.c](ex04/ft_str_is_lowercase.c) | 小文字だけかを判定 |
| ex05 | [ft_str_is_uppercase.c](ex05/ft_str_is_uppercase.c) | 大文字だけかを判定 |
| ex06 | [ft_str_is_printable.c](ex06/ft_str_is_printable.c) | 表示可能な文字だけかを判定 |
| ex07 | [ft_strupcase.c](ex07/ft_strupcase.c) | 大文字に変換 |
| ex08 | [ft_strlowcase.c](ex08/ft_strlowcase.c) | 小文字に変換 |
| ex09 | [ft_strcapitalize.c](ex09/ft_strcapitalize.c) | 単語の先頭を大文字に変換 |
| ex10 | [ft_strlcpy.c](ex10/ft_strlcpy.c) | 保存先の容量を指定してコピー |
| ex11 | [ft_putstr_non_printable.c](ex11/ft_putstr_non_printable.c) | 表示できない文字を16進数で出力 |
| ex12 | [ft_print_memory.c](ex12/ft_print_memory.c) | メモリの内容を表示（未実装） |

### ビルド例

Cコンパイラを使用し、このディレクトリで実行します。

```sh
cc -Wall -Wextra -Werror -c ex00/ft_strcpy.c -o ft_strcpy.o
```

上の例はオブジェクトファイルを生成します。関数の動作を確かめる場合は、呼び出し用の `main.c` と必要なソースを指定してリンクします。
