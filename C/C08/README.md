# Piscine C 08

## English

C exercises that put function declarations and types into headers shared by source files. They introduce macros for short expressions or constants, and structures that group multiple values.

For example, `ft_point.h` defines a type with coordinates `x` and `y`. The `ft_stock_str.h` required by the later exercises is not included.

### Exercises

| Location | Source | Behavior |
| --- | --- | --- |
| ex00 | [ft.h](ex00/ft.h) | Group function declarations |
| ex01 | [ft_boolean.h](ex01/ft_boolean.h) | Define boolean types and macros |
| ex02 | [ft_abs.h](ex02/ft_abs.h) | Define an absolute-value macro |
| ex03 | [ft_point.h](ex03/ft_point.h) | Define an x/y coordinate structure |
| ex04 | [ft_strs_to_tab.c](ex04/ft_strs_to_tab.c) | Build an array of strings and lengths; required header missing |
| ex05 | [ft_show_tab.c](ex05/ft_show_tab.c) | Display strings and lengths from structures; required header missing |

### Check a header

Use a C compiler from this directory.

```sh
cc -Wall -Wextra -Werror -x c -fsyntax-only ex00/ft.h
```

This only checks header syntax. The `ft_stock_str.h` needed by `ex04` and `ex05` is not included in this saved version.

## 日本語

関数の宣言や型をヘッダーファイルにまとめ、複数のCソースで共有する演習です。短い処理や定数を表すマクロ、複数の値を1つにまとめる構造体を扱います。

例えば `ft_point.h` は、点の座標 `x`・`y` をまとめる型を定義します。後半の演習に必要な `ft_stock_str.h` は未収録です。

### 演習

| 場所 | ソース | 処理 |
| --- | --- | --- |
| ex00 | [ft.h](ex00/ft.h) | 関数の宣言をまとめる |
| ex01 | [ft_boolean.h](ex01/ft_boolean.h) | 真偽値を扱う型・マクロを定義 |
| ex02 | [ft_abs.h](ex02/ft_abs.h) | 絶対値を計算するマクロを定義 |
| ex03 | [ft_point.h](ex03/ft_point.h) | 座標x・yを持つ構造体を定義 |
| ex04 | [ft_strs_to_tab.c](ex04/ft_strs_to_tab.c) | 文字列と長さを構造体の配列にまとめる（必要ヘッダー未収録） |
| ex05 | [ft_show_tab.c](ex05/ft_show_tab.c) | 構造体の配列から文字列と長さを表示（必要ヘッダー未収録） |

### ビルド例

Cコンパイラを使用し、このディレクトリで実行します。

```sh
cc -Wall -Wextra -Werror -x c -fsyntax-only ex00/ft.h
```

上のコマンドはヘッダーの構文確認です。`ex04`・`ex05` が参照する `ft_stock_str.h` は、この保存版には含まれていません。
