# Piscine C 07

## English

C exercises that allocate memory while running to create arrays and strings. They cover integer ranges, joining multiple strings, and splitting by delimiters.

Functions return the allocated results, which the caller releases with `free` after use. String splitting in `ex05` is still in progress.

### Exercises

| Location | Source | Behavior |
| --- | --- | --- |
| ex00 | [ft_strdup.c](ex00/ft_strdup.c) | Duplicate a string in allocated memory |
| ex01 | [ft_range.c](ex01/ft_range.c) | Create an integer range |
| ex02 | [ft_ultimate_range.c](ex02/ft_ultimate_range.c) | Create a range and return its length |
| ex03 | [ft_strjoin.c](ex03/ft_strjoin.c) | Join strings with separators |
| ex04 | [ft_convert_base.c](ex04/ft_convert_base.c), [ft_convert_base2.c](ex04/ft_convert_base2.c) | Convert numeric text between bases |
| ex05 | [ft_split.c](ex05/ft_split.c) | Split a string by delimiters; in progress |

### Compile an example

Use a C compiler from this directory.

```sh
cc -Wall -Wextra -Werror -c ex00/ft_strdup.c -o ft_strdup.o
```

This creates an object file. To run the function, link its source with a `main.c` that calls it.

## 日本語

実行中に必要な量のメモリを確保し、配列や文字列を作るC演習です。連続する整数の配列、複数の文字列の結合、区切り文字による分割などを扱います。

確保した結果を関数から返し、呼び出し側が使い終えたら `free` で解放します。文字列分割の `ex05` は実装途中です。

### 演習

| 場所 | ソース | 処理 |
| --- | --- | --- |
| ex00 | [ft_strdup.c](ex00/ft_strdup.c) | 新しいメモリに文字列を複製 |
| ex01 | [ft_range.c](ex01/ft_range.c) | 指定範囲の整数配列を作る |
| ex02 | [ft_ultimate_range.c](ex02/ft_ultimate_range.c) | 整数配列を作り、要素数も返す |
| ex03 | [ft_strjoin.c](ex03/ft_strjoin.c) | 複数の文字列を区切り文字付きで結合 |
| ex04 | [ft_convert_base.c](ex04/ft_convert_base.c)、[ft_convert_base2.c](ex04/ft_convert_base2.c) | 数値の文字列を別の基数に変換 |
| ex05 | [ft_split.c](ex05/ft_split.c) | 区切り文字で文字列を分割（実装途中） |

### ビルド例

Cコンパイラを使用し、このディレクトリで実行します。

```sh
cc -Wall -Wextra -Werror -c ex00/ft_strdup.c -o ft_strdup.o
```

上の例はオブジェクトファイルを生成します。関数の動作を確かめる場合は、呼び出し用の `main.c` と必要なソースを指定してリンクします。
