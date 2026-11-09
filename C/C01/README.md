# Piscine C 01

## English

C exercises that modify a caller's values through pointers, which identify locations in memory. Functions swap integers and reverse or sort arrays.

For example, passing the locations of `1` and `2` to `ft_swap` changes the caller's values to `2` and `1`.

### Exercises

| Location | Source | Behavior |
| --- | --- | --- |
| ex00 | [ft_ft.c](ex00/ft_ft.c) | Set a pointed-to integer to 42 |
| ex01 | [ft_ultimate_ft.c](ex01/ft_ultimate_ft.c) | Modify a value through multiple pointer levels |
| ex02 | [ft_swap.c](ex02/ft_swap.c) | Swap two integers |
| ex03 | [ft_div_mod.c](ex03/ft_div_mod.c) | Store division quotient and remainder separately |
| ex04 | [ft_ultimate_div_mod.c](ex04/ft_ultimate_div_mod.c) | Replace two integers with quotient and remainder |
| ex05 | [ft_putstr.c](ex05/ft_putstr.c) | Print a string |
| ex06 | [ft_strlen.c](ex06/ft_strlen.c) | Count characters |
| ex07 | [ft_rev_int_tab.c](ex07/ft_rev_int_tab.c) | Reverse an integer array |
| ex08 | [ft_sort_int_tab.c](ex08/ft_sort_int_tab.c) | Sort an integer array |

### Build and run

Requires a C compiler and Make.

```sh
make
make run EX=ex00
```

Combines the supplied [main.c](main.c) with each exercise to create executables such as `build/ex00`. Select an exercise with `EX` and pass runtime arguments through `ARGS`.

`ex00` sets an integer to 42 and prints it. `make run EX=ex02` prints the swapped values `2 1`.

## 日本語

関数の外にある値を、メモリ上の場所を示すポインタを通して変更するC演習です。2つの整数を交換する関数や、配列の順序を反転・整列する関数を作っています。

例えば `ft_swap` に `1` と `2` の格納先を渡すと、呼び出し元の値が `2` と `1` に入れ替わります。

### 演習

| 場所 | ソース | 処理 |
| --- | --- | --- |
| ex00 | [ft_ft.c](ex00/ft_ft.c) | ポインタの指す整数に42を代入 |
| ex01 | [ft_ultimate_ft.c](ex01/ft_ultimate_ft.c) | 多重ポインタを通して値を変更 |
| ex02 | [ft_swap.c](ex02/ft_swap.c) | 2つの整数を交換 |
| ex03 | [ft_div_mod.c](ex03/ft_div_mod.c) | 割り算の商と余りを別の変数に格納 |
| ex04 | [ft_ultimate_div_mod.c](ex04/ft_ultimate_div_mod.c) | 2つの整数を商と余りに置き換える |
| ex05 | [ft_putstr.c](ex05/ft_putstr.c) | 文字列を表示 |
| ex06 | [ft_strlen.c](ex06/ft_strlen.c) | 文字数を数える |
| ex07 | [ft_rev_int_tab.c](ex07/ft_rev_int_tab.c) | 整数配列の順序を反転 |
| ex08 | [ft_sort_int_tab.c](ex08/ft_sort_int_tab.c) | 整数配列を小さい順に整列 |

### ビルドと実行

Cコンパイラ・Make が必要です。

```sh
make
make run EX=ex00
```

付属の [main.c](main.c) と各演習のソースを組み合わせ、`build/ex00` などの実行ファイルを生成します。 `EX` で演習を選び、`ARGS` で実行時の引数を渡せます。

`ex00` の実行例は整数を42に変更して表示します。`make run EX=ex02` では、2つの整数を交換した結果の `2 1` を表示します。
